# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Practice4_pb2 as Practice4__pb2


class HelloServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.hello = channel.unary_unary(
                '/practice4.HelloService/hello',
                request_serializer=Practice4__pb2.HelloRequest.SerializeToString,
                response_deserializer=Practice4__pb2.HelloResponse.FromString,
                )


class HelloServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def hello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HelloServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'hello': grpc.unary_unary_rpc_method_handler(
                    servicer.hello,
                    request_deserializer=Practice4__pb2.HelloRequest.FromString,
                    response_serializer=Practice4__pb2.HelloResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'practice4.HelloService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HelloService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def hello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/practice4.HelloService/hello',
            Practice4__pb2.HelloRequest.SerializeToString,
            Practice4__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
