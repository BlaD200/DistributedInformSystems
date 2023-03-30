package com.vsynytsyn.distinfsystems.demo.service;

import io.grpc.stub.StreamObserver;
import org.vsynytsyn.distinfsystems.grpc.HelloThereRequest;
import org.vsynytsyn.distinfsystems.grpc.HelloThereResponse;
import org.vsynytsyn.distinfsystems.grpc.HelloThereServiceGrpc.HelloThereServiceImplBase;

public class HelloServiceImpl extends HelloThereServiceImplBase {

    @Override
    public void helloThere(HelloThereRequest request, StreamObserver<HelloThereResponse> responseObserver) {
        System.out.printf("Received request:\n'%s'\n", request.toString());
        String greeting = "Hello, " + request.getName() + " " + request.getSurname();

        HelloThereResponse response = HelloThereResponse.newBuilder()
                .setMessage(greeting)
                .build();

        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }
}
