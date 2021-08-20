# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import database_pb2 as database__pb2


class DatabaseStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/Database/CreateUser',
                request_serializer=database__pb2.User.SerializeToString,
                response_deserializer=database__pb2.UserResponse.FromString,
                )
        self.GetUser = channel.unary_unary(
                '/Database/GetUser',
                request_serializer=database__pb2.User.SerializeToString,
                response_deserializer=database__pb2.UserResponse.FromString,
                )
        self.GetAllUsers = channel.unary_unary(
                '/Database/GetAllUsers',
                request_serializer=database__pb2.User.SerializeToString,
                response_deserializer=database__pb2.UserResponse.FromString,
                )
        self.GetUserByUserName = channel.unary_unary(
                '/Database/GetUserByUserName',
                request_serializer=database__pb2.User.SerializeToString,
                response_deserializer=database__pb2.UserResponse.FromString,
                )
        self.GetUserByEmail = channel.unary_unary(
                '/Database/GetUserByEmail',
                request_serializer=database__pb2.User.SerializeToString,
                response_deserializer=database__pb2.UserResponse.FromString,
                )


class DatabaseServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserByUserName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserByEmail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DatabaseServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=database__pb2.User.FromString,
                    response_serializer=database__pb2.UserResponse.SerializeToString,
            ),
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=database__pb2.User.FromString,
                    response_serializer=database__pb2.UserResponse.SerializeToString,
            ),
            'GetAllUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllUsers,
                    request_deserializer=database__pb2.User.FromString,
                    response_serializer=database__pb2.UserResponse.SerializeToString,
            ),
            'GetUserByUserName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByUserName,
                    request_deserializer=database__pb2.User.FromString,
                    response_serializer=database__pb2.UserResponse.SerializeToString,
            ),
            'GetUserByEmail': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByEmail,
                    request_deserializer=database__pb2.User.FromString,
                    response_serializer=database__pb2.UserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Database', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Database(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Database/CreateUser',
            database__pb2.User.SerializeToString,
            database__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Database/GetUser',
            database__pb2.User.SerializeToString,
            database__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Database/GetAllUsers',
            database__pb2.User.SerializeToString,
            database__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserByUserName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Database/GetUserByUserName',
            database__pb2.User.SerializeToString,
            database__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserByEmail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Database/GetUserByEmail',
            database__pb2.User.SerializeToString,
            database__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)