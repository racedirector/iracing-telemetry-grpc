import grpc
import json
import struct
import yaml
from google.protobuf.struct_pb2 import Struct
from irsdk import IRSDK, VAR_TYPE_MAP, YAML_CODE_PAGE
from server.date_encoder import DateEncoder
from server.iracing_service import IRacingService
from server.proto import telemetry_pb2
from server.proto import telemetry_pb2_grpc
from time import sleep
from typing import Iterable

try:
    from yaml.cyaml import CSafeLoader as YamlSafeLoader
except ImportError:
    from yaml import SafeLoader as YamlSafeLoader

class TelemetryService(IRacingService, telemetry_pb2_grpc.TelemetryServicer):
  """Servicer that manages telemetry data."""

  session_json_schema = {}
  telemetry_json_schema = {}

  def __init__(self, ir: IRSDK):
    super().__init__(ir)

  def DumpTelemetry(self, request, context):
    response = telemetry_pb2.GetTelemetryResponse()
    if self.check_is_connected(context):
      response_data = Struct()
      telemetry_cache = {}

      self.ir.freeze_var_buffer_latest()
      session_binary = self.ir._shared_mem[self.ir._header.session_info_offset:self.ir._header.session_info_len].rstrip(b'\x00').decode(YAML_CODE_PAGE)
      
      # Get all the headers from the buffer
      for key in self.ir._var_headers_dict:
        var_header = self.ir._var_headers_dict[key]
        var_buf_latest = self.ir._var_buffer_latest
        res = struct.unpack_from(
          VAR_TYPE_MAP[var_header.type] * var_header.count,
          var_buf_latest.get_memory(),
          var_buf_latest.buf_offset + var_header.offset)
        
        telemetry_cache[key] = res[0] if var_header.count == 1 else list(res)

      self.ir.unfreeze_var_buffer_latest()

      # Convert the binary session info to a JSON dictionary
      session_yml = yaml.load(session_binary, Loader=YamlSafeLoader)
      session_json_string = json.dumps(session_yml, indent=2, default=DateEncoder)
      session_json = json.loads(session_json_string)

      # Update the response
      response_data.update(session_json)
      response_data.update(telemetry_cache)
      response.telemetry = response_data
    
    return response

  def GetTelemetry(self, request: telemetry_pb2.GetTelemetryRequest, context: grpc.ServicerContext) -> telemetry_pb2.GetTelemetryResponse:
    response = telemetry_pb2.GetTelemetryResponse()
    if self.check_is_connected(context):
      self.ir.freeze_var_buffer_latest()
      telemetry = { 
        key: self.ir[key]
        for key in request.keys
      }
      self.ir.unfreeze_var_buffer_latest()

      struct = Struct()
      struct.update(telemetry)
      response.telemetry = struct

    return response
  
  def RequestTelemetryStream(self, request_iterator: Iterable[telemetry_pb2.GetTelemetryRequest], context: grpc.ServicerContext) -> Iterable[telemetry_pb2.GetTelemetryResponse]:
    return super().RequestTelemetryStream(request_iterator, context)
  
  def SubscribeTelemetryStream(self, request: telemetry_pb2.TelemetrySubscriptionRequest, context: grpc.ServicerContext) -> Iterable[telemetry_pb2.GetTelemetryResponse]:
    fps = request.fps
    if fps <= 0:
      context.set_details("FPS must be greater than 0")
      context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
      return telemetry_pb2.GetTelemetryResponse()
    if fps > 60:
      context.set_details("FPS must be less than or equal to 60")
      context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
      return telemetry_pb2.GetTelemetryResponse()
    if not request.keys:
      context.set_details("Keys must not be empty")
      context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
      return telemetry_pb2.GetTelemetryResponse()

    '''
    For a telemetry subscription, we create a new instance of pyirsdk
    so the buffers can be frozen and unfrozen without affecting the main instance.
    This is important because the main instance is used for other purposes
    and we don't want to interfere with its operation.
    '''
    stream_ir = IRSDK()
    if not stream_ir.startup():
      context.set_details("Failed to connect to iRacing")
      context.set_code(grpc.StatusCode.UNAVAILABLE)
      return telemetry_pb2.GetTelemetryResponse()
    
    # Shutdown the connection to iRacing when the stream is closed.
    context.add_callback(stream_ir.shutdown)

    telemetry_cache = {}
    while stream_ir.is_connected and stream_ir.is_initialized:
      stream_ir.freeze_var_buffer_latest()
      telemetry = { 
        key: stream_ir[key]
        for key in request.keys 
        if key not in telemetry_cache or telemetry_cache[key] != stream_ir[key] 
      }
      stream_ir.unfreeze_var_buffer_latest()

      if telemetry: 
        struct = Struct()
        struct.update(telemetry)
        yield telemetry_pb2.GetTelemetryResponse(telemetry=struct)
        telemetry_cache.update(telemetry)

      # Update the cache and sleep
      sleep(1 / fps)

    context.set_details("iRacing disconnected")
    return telemetry_pb2.GetTelemetryResponse()
  
