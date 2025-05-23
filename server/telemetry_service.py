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

def get_telemetry_from_iracing(ir: IRSDK, keys: list[str], condition = lambda key: True) -> dict:
  telemetry = {}
  ir.freeze_var_buffer_latest()
  telemetry = { 
    key: ir[key]
    for key in keys
    if condition(key)
  }
  ir.unfreeze_var_buffer_latest()

  return telemetry


class TelemetryService(IRacingService, telemetry_pb2_grpc.TelemetryServicer):
  """Servicer that manages telemetry data."""

  def __init__(self, ir: IRSDK, test_file=None):
    super().__init__(ir)
    self.test_file = test_file

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

  def DumpTelemetryString(self, request, context):
    response = telemetry_pb2.GetTelemetryStringResponse()
    if self.check_is_connected(context):
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

      telemetry_cache.update(session_json)
      response.telemetry = json.dumps(telemetry_cache, default=DateEncoder)
    
    return response

  def GetTelemetry(self, request: telemetry_pb2.GetTelemetryRequest, context: grpc.ServicerContext) -> telemetry_pb2.GetTelemetryResponse:
    response = telemetry_pb2.GetTelemetryResponse()
    if self.check_is_connected(context):
      telemetry = get_telemetry_from_iracing(self.ir, request.keys)

      struct = Struct()
      struct.update(telemetry)
      response.telemetry = struct

    return response
  
  def GetTelemetryString(self, request: telemetry_pb2.GetTelemetryRequest, context):
    response = telemetry_pb2.GetTelemetryStringResponse()
    if self.check_is_connected(context):
      telemetry = get_telemetry_from_iracing(self.ir, request.keys)
      response.telemetry = json.dumps(telemetry, default=DateEncoder)

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
    if not stream_ir.startup(test_file=self.test_file):
      context.set_details("Failed to connect to iRacing")
      context.set_code(grpc.StatusCode.UNAVAILABLE)
      return telemetry_pb2.GetTelemetryResponse()
    
    # Shutdown the connection to iRacing when the stream is closed.
    context.add_callback(stream_ir.shutdown)

    telemetry_cache = {}
    while stream_ir.is_connected and stream_ir.is_initialized:
      telemetry = get_telemetry_from_iracing(
        stream_ir,
        request.keys, 
        lambda key: key not in telemetry_cache or telemetry_cache[key] != stream_ir[key]
      )

      if telemetry: 
        struct = Struct()
        struct.update(telemetry)
        yield telemetry_pb2.GetTelemetryResponse(telemetry=struct)
        telemetry_cache.update(telemetry)

      # Update the cache and sleep
      sleep(1 / fps)

    context.set_details("iRacing disconnected")
    return telemetry_pb2.GetTelemetryResponse()
  
  def SubscribeTelemetryStringStream(self, request: telemetry_pb2.TelemetrySubscriptionRequest, context: grpc.ServicerContext):
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
    if not stream_ir.startup(test_file=self.test_file):
      context.set_details("Failed to connect to iRacing")
      context.set_code(grpc.StatusCode.UNAVAILABLE)
      return telemetry_pb2.GetTelemetryResponse()
    
    # Shutdown the connection to iRacing when the stream is closed.
    context.add_callback(stream_ir.shutdown)

    telemetry_cache = {}
    while stream_ir.is_connected and stream_ir.is_initialized:
      telemetry = get_telemetry_from_iracing(
        stream_ir,
        request.keys, 
        lambda key: key not in telemetry_cache or telemetry_cache[key] != stream_ir[key]
      )

      if telemetry: 
        yield telemetry_pb2.GetTelemetryStringResponse(
          telemetry=json.dumps(telemetry, default=DateEncoder)
        )

      # Update the cache and sleep
      sleep(1 / fps)

    context.set_details("iRacing disconnected")
    return telemetry_pb2.GetTelemetryResponse()
