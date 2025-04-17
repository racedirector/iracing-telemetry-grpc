# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from server.proto import telemetry_pb2 as server_dot_proto_dot_telemetry__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in server/proto/telemetry_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TelemetryStub(object):
    """
    A service for interacting with iRacing telemetry.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTelemetryTypes = channel.unary_unary(
                '/iracing.telemetry.Telemetry/GetTelemetryTypes',
                request_serializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryTypesRequest.SerializeToString,
                response_deserializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryTypesResponse.FromString,
                _registered_method=True)
        self.GetTelemetryJSONSchema = channel.unary_unary(
                '/iracing.telemetry.Telemetry/GetTelemetryJSONSchema',
                request_serializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryTypesRequest.SerializeToString,
                response_deserializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryJSONSchemaResponse.FromString,
                _registered_method=True)
        self.GetTelemetryJSONSchemaString = channel.unary_unary(
                '/iracing.telemetry.Telemetry/GetTelemetryJSONSchemaString',
                request_serializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryTypesRequest.SerializeToString,
                response_deserializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryJSONSchemaStringResponse.FromString,
                _registered_method=True)
        self.DumpTelemetry = channel.unary_unary(
                '/iracing.telemetry.Telemetry/DumpTelemetry',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryResponse.FromString,
                _registered_method=True)
        self.GetTelemetry = channel.unary_unary(
                '/iracing.telemetry.Telemetry/GetTelemetry',
                request_serializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryRequest.SerializeToString,
                response_deserializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryResponse.FromString,
                _registered_method=True)
        self.RequestTelemetryStream = channel.stream_stream(
                '/iracing.telemetry.Telemetry/RequestTelemetryStream',
                request_serializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryRequest.SerializeToString,
                response_deserializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryResponse.FromString,
                _registered_method=True)
        self.SubscribeTelemetryStream = channel.unary_stream(
                '/iracing.telemetry.Telemetry/SubscribeTelemetryStream',
                request_serializer=server_dot_proto_dot_telemetry__pb2.TelemetrySubscriptionRequest.SerializeToString,
                response_deserializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryResponse.FromString,
                _registered_method=True)


class TelemetryServicer(object):
    """
    A service for interacting with iRacing telemetry.
    """

    def GetTelemetryTypes(self, request, context):
        """
        A server-to-client RPC

        The client sends a GetTelemetryTypesRequest message to the server and
        the server responds with a dictionary of telemetry keys and their types.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTelemetryJSONSchema(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTelemetryJSONSchemaString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DumpTelemetry(self, request, context):
        """
        A server-to-client RPC

        The client sends an Empty message to the server and receives all telemetry
        data in the current buffer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTelemetry(self, request, context):
        """
        A server-to-client RPC

        The client sends a GetTelemetryRequest message to the server and gets a
        single GetTelemetryResponse message back.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestTelemetryStream(self, request_iterator, context):
        """
        A client-to-server bidirectional streaming RPC

        The client sends a GetTelemetryRequest message each time it wants a new
        telemetry item. Useful when the client wants to control it's own cadence
        for iteration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeTelemetryStream(self, request, context):
        """
        A client-to-server streaming RPC

        The client sends a TelemetrySubscriptionRequest message to the server and
        gets a stream back at their requested FPS. Only changed values are sent
        over the stream after the initial message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TelemetryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTelemetryTypes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTelemetryTypes,
                    request_deserializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryTypesRequest.FromString,
                    response_serializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryTypesResponse.SerializeToString,
            ),
            'GetTelemetryJSONSchema': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTelemetryJSONSchema,
                    request_deserializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryTypesRequest.FromString,
                    response_serializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryJSONSchemaResponse.SerializeToString,
            ),
            'GetTelemetryJSONSchemaString': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTelemetryJSONSchemaString,
                    request_deserializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryTypesRequest.FromString,
                    response_serializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryJSONSchemaStringResponse.SerializeToString,
            ),
            'DumpTelemetry': grpc.unary_unary_rpc_method_handler(
                    servicer.DumpTelemetry,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryResponse.SerializeToString,
            ),
            'GetTelemetry': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTelemetry,
                    request_deserializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryRequest.FromString,
                    response_serializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryResponse.SerializeToString,
            ),
            'RequestTelemetryStream': grpc.stream_stream_rpc_method_handler(
                    servicer.RequestTelemetryStream,
                    request_deserializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryRequest.FromString,
                    response_serializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryResponse.SerializeToString,
            ),
            'SubscribeTelemetryStream': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeTelemetryStream,
                    request_deserializer=server_dot_proto_dot_telemetry__pb2.TelemetrySubscriptionRequest.FromString,
                    response_serializer=server_dot_proto_dot_telemetry__pb2.GetTelemetryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'iracing.telemetry.Telemetry', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('iracing.telemetry.Telemetry', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Telemetry(object):
    """
    A service for interacting with iRacing telemetry.
    """

    @staticmethod
    def GetTelemetryTypes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/iracing.telemetry.Telemetry/GetTelemetryTypes',
            server_dot_proto_dot_telemetry__pb2.GetTelemetryTypesRequest.SerializeToString,
            server_dot_proto_dot_telemetry__pb2.GetTelemetryTypesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTelemetryJSONSchema(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/iracing.telemetry.Telemetry/GetTelemetryJSONSchema',
            server_dot_proto_dot_telemetry__pb2.GetTelemetryTypesRequest.SerializeToString,
            server_dot_proto_dot_telemetry__pb2.GetTelemetryJSONSchemaResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTelemetryJSONSchemaString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/iracing.telemetry.Telemetry/GetTelemetryJSONSchemaString',
            server_dot_proto_dot_telemetry__pb2.GetTelemetryTypesRequest.SerializeToString,
            server_dot_proto_dot_telemetry__pb2.GetTelemetryJSONSchemaStringResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DumpTelemetry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/iracing.telemetry.Telemetry/DumpTelemetry',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            server_dot_proto_dot_telemetry__pb2.GetTelemetryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTelemetry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/iracing.telemetry.Telemetry/GetTelemetry',
            server_dot_proto_dot_telemetry__pb2.GetTelemetryRequest.SerializeToString,
            server_dot_proto_dot_telemetry__pb2.GetTelemetryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RequestTelemetryStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/iracing.telemetry.Telemetry/RequestTelemetryStream',
            server_dot_proto_dot_telemetry__pb2.GetTelemetryRequest.SerializeToString,
            server_dot_proto_dot_telemetry__pb2.GetTelemetryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SubscribeTelemetryStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/iracing.telemetry.Telemetry/SubscribeTelemetryStream',
            server_dot_proto_dot_telemetry__pb2.TelemetrySubscriptionRequest.SerializeToString,
            server_dot_proto_dot_telemetry__pb2.GetTelemetryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
