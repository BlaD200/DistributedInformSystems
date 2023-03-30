package com.vsynytsyn.distinfsystems.demo.service;

import io.grpc.stub.StreamObserver;
import org.vsynytsyn.distinfsystems.grpc.HelloRequest;
import org.vsynytsyn.distinfsystems.grpc.HelloResponse;
import org.vsynytsyn.distinfsystems.grpc.HelloServiceGrpc.HelloServiceImplBase;

public class HelloServiceImpl extends HelloServiceImplBase {

    @Override
    public void hello(
            HelloRequest request, StreamObserver<HelloResponse> responseObserver) {

        String greeting = "Hello, " + request.getFirstName() + " " + request.getLastName();

        HelloResponse response = HelloResponse.newBuilder()
                .setGreeting(greeting)
                .build();

        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }
}
