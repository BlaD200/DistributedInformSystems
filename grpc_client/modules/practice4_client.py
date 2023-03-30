from __future__ import print_function

import logging

import grpc
import Practice4_pb2
import Practice4_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = Practice4_pb2_grpc.HelloServiceStub(channel)
        response = stub.hello(Practice4_pb2.HelloRequest(firstName='Diya', lastName='Nadiya'))
    print("Client received: " + response.greeting)


if __name__ == '__main__':
    logging.basicConfig()
    run()
