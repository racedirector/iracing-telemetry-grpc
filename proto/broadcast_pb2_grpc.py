# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import broadcast_pb2 as broadcast__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

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
        + f' but the generated code in broadcast_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAvailableCameras = channel.unary_unary(
                '/iracing.broadcast_message.Server/GetAvailableCameras',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=broadcast__pb2.GetAvailableCamerasResponse.FromString,
                _registered_method=True)
        self.CameraSwitchPosition = channel.unary_unary(
                '/iracing.broadcast_message.Server/CameraSwitchPosition',
                request_serializer=broadcast__pb2.CameraSwitchPositionRequest.SerializeToString,
                response_deserializer=broadcast__pb2.CameraSwitchPositionResponse.FromString,
                _registered_method=True)
        self.CameraSwitchNumber = channel.unary_unary(
                '/iracing.broadcast_message.Server/CameraSwitchNumber',
                request_serializer=broadcast__pb2.CameraSwitchNumberRequest.SerializeToString,
                response_deserializer=broadcast__pb2.CameraSwitchNumberResponse.FromString,
                _registered_method=True)
        self.CameraSetState = channel.unary_unary(
                '/iracing.broadcast_message.Server/CameraSetState',
                request_serializer=broadcast__pb2.CameraSetStateRequest.SerializeToString,
                response_deserializer=broadcast__pb2.CameraSetStateResponse.FromString,
                _registered_method=True)
        self.ReplaySetPlaySpeed = channel.unary_unary(
                '/iracing.broadcast_message.Server/ReplaySetPlaySpeed',
                request_serializer=broadcast__pb2.ReplaySetPlaySpeedRequest.SerializeToString,
                response_deserializer=broadcast__pb2.ReplaySetPlaySpeedResponse.FromString,
                _registered_method=True)
        self.ReplaySetPlayPosition = channel.unary_unary(
                '/iracing.broadcast_message.Server/ReplaySetPlayPosition',
                request_serializer=broadcast__pb2.ReplaySetPlayPositionRequest.SerializeToString,
                response_deserializer=broadcast__pb2.ReplaySetPlayPositionResponse.FromString,
                _registered_method=True)
        self.ReplaySearch = channel.unary_unary(
                '/iracing.broadcast_message.Server/ReplaySearch',
                request_serializer=broadcast__pb2.ReplaySearchRequest.SerializeToString,
                response_deserializer=broadcast__pb2.ReplaySearchResponse.FromString,
                _registered_method=True)
        self.ReplaySetState = channel.unary_unary(
                '/iracing.broadcast_message.Server/ReplaySetState',
                request_serializer=broadcast__pb2.ReplaySetStateRequest.SerializeToString,
                response_deserializer=broadcast__pb2.ReplaySetStateResponse.FromString,
                _registered_method=True)
        self.ReloadTextures = channel.unary_unary(
                '/iracing.broadcast_message.Server/ReloadTextures',
                request_serializer=broadcast__pb2.ReloadTexturesRequest.SerializeToString,
                response_deserializer=broadcast__pb2.ReloadTexturesResponse.FromString,
                _registered_method=True)
        self.ChatCommand = channel.unary_unary(
                '/iracing.broadcast_message.Server/ChatCommand',
                request_serializer=broadcast__pb2.ChatCommandRequest.SerializeToString,
                response_deserializer=broadcast__pb2.ChatCommandResponse.FromString,
                _registered_method=True)
        self.PitCommand = channel.unary_unary(
                '/iracing.broadcast_message.Server/PitCommand',
                request_serializer=broadcast__pb2.PitCommandRequest.SerializeToString,
                response_deserializer=broadcast__pb2.PitCommandResponse.FromString,
                _registered_method=True)
        self.TelemetryCommand = channel.unary_unary(
                '/iracing.broadcast_message.Server/TelemetryCommand',
                request_serializer=broadcast__pb2.TelemetryCommandRequest.SerializeToString,
                response_deserializer=broadcast__pb2.TelemetryCommandResponse.FromString,
                _registered_method=True)
        self.ForceFeedbackCommand = channel.unary_unary(
                '/iracing.broadcast_message.Server/ForceFeedbackCommand',
                request_serializer=broadcast__pb2.ForceFeedbackCommandRequest.SerializeToString,
                response_deserializer=broadcast__pb2.ForceFeedbackCommandResponse.FromString,
                _registered_method=True)
        self.ReplaySearchSessionTime = channel.unary_unary(
                '/iracing.broadcast_message.Server/ReplaySearchSessionTime',
                request_serializer=broadcast__pb2.ReplaySearchSessionTimeRequest.SerializeToString,
                response_deserializer=broadcast__pb2.ReplaySearchSessionTimeResponse.FromString,
                _registered_method=True)
        self.VideoCapture = channel.unary_unary(
                '/iracing.broadcast_message.Server/VideoCapture',
                request_serializer=broadcast__pb2.VideoCaptureRequest.SerializeToString,
                response_deserializer=broadcast__pb2.VideoCaptureResponse.FromString,
                _registered_method=True)


class ServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAvailableCameras(self, request, context):
        """A client-to-server RPC

        Returns the available camera groups and cameras per-group,
        as well as the current camera information.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CameraSwitchPosition(self, request, context):
        """A client-to-server RPC

        Switches the camera to a new position. Returns the new camera position.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CameraSwitchNumber(self, request, context):
        """A client-to-server RPC

        Switches the camera to a new number. Returns the new camera position.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CameraSetState(self, request, context):
        """A client-to-server RPC

        Sets the state of the camera
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplaySetPlaySpeed(self, request, context):
        """A client-to-server RPC

        Sets the play speed of the replay
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplaySetPlayPosition(self, request, context):
        """A client-to-server RPC

        Sets the play position of the replay
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplaySearch(self, request, context):
        """A client-to-server RPC

        Searches the replay
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplaySetState(self, request, context):
        """A client-to-server RPC

        Sets the state of the replay
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReloadTextures(self, request, context):
        """A client-to-server RPC

        Reloads the textures
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChatCommand(self, request, context):
        """A client-to-server RPC

        Sends a chat command
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PitCommand(self, request, context):
        """A client-to-server RPC

        Sends a pit command
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TelemetryCommand(self, request, context):
        """A client-to-server RPC

        Sends a telemetry command
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ForceFeedbackCommand(self, request, context):
        """A client-to-server RPC

        Sends a force feedback command
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplaySearchSessionTime(self, request, context):
        """A client-to-server RPC

        Searches the replay by session time
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VideoCapture(self, request, context):
        """A client-to-server RPC

        Captures video
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAvailableCameras': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAvailableCameras,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=broadcast__pb2.GetAvailableCamerasResponse.SerializeToString,
            ),
            'CameraSwitchPosition': grpc.unary_unary_rpc_method_handler(
                    servicer.CameraSwitchPosition,
                    request_deserializer=broadcast__pb2.CameraSwitchPositionRequest.FromString,
                    response_serializer=broadcast__pb2.CameraSwitchPositionResponse.SerializeToString,
            ),
            'CameraSwitchNumber': grpc.unary_unary_rpc_method_handler(
                    servicer.CameraSwitchNumber,
                    request_deserializer=broadcast__pb2.CameraSwitchNumberRequest.FromString,
                    response_serializer=broadcast__pb2.CameraSwitchNumberResponse.SerializeToString,
            ),
            'CameraSetState': grpc.unary_unary_rpc_method_handler(
                    servicer.CameraSetState,
                    request_deserializer=broadcast__pb2.CameraSetStateRequest.FromString,
                    response_serializer=broadcast__pb2.CameraSetStateResponse.SerializeToString,
            ),
            'ReplaySetPlaySpeed': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplaySetPlaySpeed,
                    request_deserializer=broadcast__pb2.ReplaySetPlaySpeedRequest.FromString,
                    response_serializer=broadcast__pb2.ReplaySetPlaySpeedResponse.SerializeToString,
            ),
            'ReplaySetPlayPosition': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplaySetPlayPosition,
                    request_deserializer=broadcast__pb2.ReplaySetPlayPositionRequest.FromString,
                    response_serializer=broadcast__pb2.ReplaySetPlayPositionResponse.SerializeToString,
            ),
            'ReplaySearch': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplaySearch,
                    request_deserializer=broadcast__pb2.ReplaySearchRequest.FromString,
                    response_serializer=broadcast__pb2.ReplaySearchResponse.SerializeToString,
            ),
            'ReplaySetState': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplaySetState,
                    request_deserializer=broadcast__pb2.ReplaySetStateRequest.FromString,
                    response_serializer=broadcast__pb2.ReplaySetStateResponse.SerializeToString,
            ),
            'ReloadTextures': grpc.unary_unary_rpc_method_handler(
                    servicer.ReloadTextures,
                    request_deserializer=broadcast__pb2.ReloadTexturesRequest.FromString,
                    response_serializer=broadcast__pb2.ReloadTexturesResponse.SerializeToString,
            ),
            'ChatCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.ChatCommand,
                    request_deserializer=broadcast__pb2.ChatCommandRequest.FromString,
                    response_serializer=broadcast__pb2.ChatCommandResponse.SerializeToString,
            ),
            'PitCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.PitCommand,
                    request_deserializer=broadcast__pb2.PitCommandRequest.FromString,
                    response_serializer=broadcast__pb2.PitCommandResponse.SerializeToString,
            ),
            'TelemetryCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.TelemetryCommand,
                    request_deserializer=broadcast__pb2.TelemetryCommandRequest.FromString,
                    response_serializer=broadcast__pb2.TelemetryCommandResponse.SerializeToString,
            ),
            'ForceFeedbackCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.ForceFeedbackCommand,
                    request_deserializer=broadcast__pb2.ForceFeedbackCommandRequest.FromString,
                    response_serializer=broadcast__pb2.ForceFeedbackCommandResponse.SerializeToString,
            ),
            'ReplaySearchSessionTime': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplaySearchSessionTime,
                    request_deserializer=broadcast__pb2.ReplaySearchSessionTimeRequest.FromString,
                    response_serializer=broadcast__pb2.ReplaySearchSessionTimeResponse.SerializeToString,
            ),
            'VideoCapture': grpc.unary_unary_rpc_method_handler(
                    servicer.VideoCapture,
                    request_deserializer=broadcast__pb2.VideoCaptureRequest.FromString,
                    response_serializer=broadcast__pb2.VideoCaptureResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'iracing.broadcast_message.Server', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('iracing.broadcast_message.Server', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Server(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAvailableCameras(request,
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
            '/iracing.broadcast_message.Server/GetAvailableCameras',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            broadcast__pb2.GetAvailableCamerasResponse.FromString,
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
    def CameraSwitchPosition(request,
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
            '/iracing.broadcast_message.Server/CameraSwitchPosition',
            broadcast__pb2.CameraSwitchPositionRequest.SerializeToString,
            broadcast__pb2.CameraSwitchPositionResponse.FromString,
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
    def CameraSwitchNumber(request,
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
            '/iracing.broadcast_message.Server/CameraSwitchNumber',
            broadcast__pb2.CameraSwitchNumberRequest.SerializeToString,
            broadcast__pb2.CameraSwitchNumberResponse.FromString,
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
    def CameraSetState(request,
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
            '/iracing.broadcast_message.Server/CameraSetState',
            broadcast__pb2.CameraSetStateRequest.SerializeToString,
            broadcast__pb2.CameraSetStateResponse.FromString,
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
    def ReplaySetPlaySpeed(request,
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
            '/iracing.broadcast_message.Server/ReplaySetPlaySpeed',
            broadcast__pb2.ReplaySetPlaySpeedRequest.SerializeToString,
            broadcast__pb2.ReplaySetPlaySpeedResponse.FromString,
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
    def ReplaySetPlayPosition(request,
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
            '/iracing.broadcast_message.Server/ReplaySetPlayPosition',
            broadcast__pb2.ReplaySetPlayPositionRequest.SerializeToString,
            broadcast__pb2.ReplaySetPlayPositionResponse.FromString,
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
    def ReplaySearch(request,
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
            '/iracing.broadcast_message.Server/ReplaySearch',
            broadcast__pb2.ReplaySearchRequest.SerializeToString,
            broadcast__pb2.ReplaySearchResponse.FromString,
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
    def ReplaySetState(request,
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
            '/iracing.broadcast_message.Server/ReplaySetState',
            broadcast__pb2.ReplaySetStateRequest.SerializeToString,
            broadcast__pb2.ReplaySetStateResponse.FromString,
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
    def ReloadTextures(request,
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
            '/iracing.broadcast_message.Server/ReloadTextures',
            broadcast__pb2.ReloadTexturesRequest.SerializeToString,
            broadcast__pb2.ReloadTexturesResponse.FromString,
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
    def ChatCommand(request,
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
            '/iracing.broadcast_message.Server/ChatCommand',
            broadcast__pb2.ChatCommandRequest.SerializeToString,
            broadcast__pb2.ChatCommandResponse.FromString,
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
    def PitCommand(request,
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
            '/iracing.broadcast_message.Server/PitCommand',
            broadcast__pb2.PitCommandRequest.SerializeToString,
            broadcast__pb2.PitCommandResponse.FromString,
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
    def TelemetryCommand(request,
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
            '/iracing.broadcast_message.Server/TelemetryCommand',
            broadcast__pb2.TelemetryCommandRequest.SerializeToString,
            broadcast__pb2.TelemetryCommandResponse.FromString,
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
    def ForceFeedbackCommand(request,
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
            '/iracing.broadcast_message.Server/ForceFeedbackCommand',
            broadcast__pb2.ForceFeedbackCommandRequest.SerializeToString,
            broadcast__pb2.ForceFeedbackCommandResponse.FromString,
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
    def ReplaySearchSessionTime(request,
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
            '/iracing.broadcast_message.Server/ReplaySearchSessionTime',
            broadcast__pb2.ReplaySearchSessionTimeRequest.SerializeToString,
            broadcast__pb2.ReplaySearchSessionTimeResponse.FromString,
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
    def VideoCapture(request,
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
            '/iracing.broadcast_message.Server/VideoCapture',
            broadcast__pb2.VideoCaptureRequest.SerializeToString,
            broadcast__pb2.VideoCaptureResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
