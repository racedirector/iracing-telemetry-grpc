# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import telemetry_pb2 as telemetry__pb2

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
        + f' but the generated code in telemetry_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TelemetryStub(object):
    """A service for interacting with iRacing telemetry.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTelemetry = channel.unary_unary(
                '/iracing.telemetry.Telemetry/GetTelemetry',
                request_serializer=telemetry__pb2.GetTelemetryRequest.SerializeToString,
                response_deserializer=telemetry__pb2.GetTelemetryResponse.FromString,
                _registered_method=True)
        self.RequestTelemetryStream = channel.stream_stream(
                '/iracing.telemetry.Telemetry/RequestTelemetryStream',
                request_serializer=telemetry__pb2.GetTelemetryRequest.SerializeToString,
                response_deserializer=telemetry__pb2.GetTelemetryResponse.FromString,
                _registered_method=True)
        self.SubscribeTelemetryStream = channel.unary_stream(
                '/iracing.telemetry.Telemetry/SubscribeTelemetryStream',
                request_serializer=telemetry__pb2.TelemetrySubscriptionRequest.SerializeToString,
                response_deserializer=telemetry__pb2.GetTelemetryResponse.FromString,
                _registered_method=True)


class TelemetryServicer(object):
    """A service for interacting with iRacing telemetry.
    """

    def GetTelemetry(self, request, context):
        """A server-to-client RPC

        The client sends a GetTelemetryRequest message to the server and gets a
        single GetTelemetryResponse message back.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestTelemetryStream(self, request_iterator, context):
        """A client-to-server bidirectional streaming RPC

        The client sends a GetTelemetryRequest message each time it wants a new
        telemetry item. Useful when the client wants to control it's own cadence for iteration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeTelemetryStream(self, request, context):
        """A client-to-server streaming RPC

        The client sends a TelemetrySubscriptionRequest message to the server and
        gets a stream back at their requested FPS. Only changed values are sent
        over the stream after the initial message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TelemetryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTelemetry': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTelemetry,
                    request_deserializer=telemetry__pb2.GetTelemetryRequest.FromString,
                    response_serializer=telemetry__pb2.GetTelemetryResponse.SerializeToString,
            ),
            'RequestTelemetryStream': grpc.stream_stream_rpc_method_handler(
                    servicer.RequestTelemetryStream,
                    request_deserializer=telemetry__pb2.GetTelemetryRequest.FromString,
                    response_serializer=telemetry__pb2.GetTelemetryResponse.SerializeToString,
            ),
            'SubscribeTelemetryStream': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeTelemetryStream,
                    request_deserializer=telemetry__pb2.TelemetrySubscriptionRequest.FromString,
                    response_serializer=telemetry__pb2.GetTelemetryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'iracing.telemetry.Telemetry', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('iracing.telemetry.Telemetry', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Telemetry(object):
    """A service for interacting with iRacing telemetry.
    """

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
            telemetry__pb2.GetTelemetryRequest.SerializeToString,
            telemetry__pb2.GetTelemetryResponse.FromString,
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
            telemetry__pb2.GetTelemetryRequest.SerializeToString,
            telemetry__pb2.GetTelemetryResponse.FromString,
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
            telemetry__pb2.TelemetrySubscriptionRequest.SerializeToString,
            telemetry__pb2.GetTelemetryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
