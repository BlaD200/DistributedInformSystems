from __future__ import print_function


import grpc
import Practice4_pb2
import Practice4_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = Practice4_pb2_grpc.HelloThereServiceStub(channel)
        response = stub.hello_there(Practice4_pb2.HelloThereRequest(name='Diya', surname='Nadiya'))
    print("Client received: " + response.message)


if __name__ == '__main__':
    run()
