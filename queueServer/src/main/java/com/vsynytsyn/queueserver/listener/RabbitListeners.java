package com.vsynytsyn.queueserver.listener;


import com.fasterxml.jackson.databind.ObjectMapper;
import com.vsynytsyn.queueserver.dto.RabbitMessageDto;
import com.vsynytsyn.queueserver.service.LogProcessingService;
import org.springframework.amqp.rabbit.annotation.EnableRabbit;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.io.IOException;

@Component
@EnableRabbit
public class RabbitListeners {

    private final ObjectMapper objectMapper;
    private final LogProcessingService processingService;


    @Autowired
    public RabbitListeners(ObjectMapper objectMapper, LogProcessingService processingService) {
        this.objectMapper = objectMapper;
        this.processingService = processingService;
    }


    @RabbitListener(queues = "LogDebugProcessingQueue")
    public void processLogDebug(byte[] message) {
        try {
            RabbitMessageDto messageDTO = objectMapper.readValue(message, RabbitMessageDto.class);
            processingService.processLog(
                    messageDTO.getHashValue(),
                    messageDTO.getMessage(),
                    messageDTO.getTimestamp(),
                    LogProcessingService.LogLevels.DEBUG
            );
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @RabbitListener(queues = "LogInfoProcessingQueue")
    public void processLogInfo(byte[] message) {
        try {
            RabbitMessageDto messageDTO = objectMapper.readValue(message, RabbitMessageDto.class);
            processingService.processLog(
                    messageDTO.getHashValue(),
                    messageDTO.getMessage(),
                    messageDTO.getTimestamp(),
                    LogProcessingService.LogLevels.INFO
            );
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

//    @RabbitListener(queues = "LogProcessedQueue")
//    public void processedLogInfo(String processedHash) {
//        System.out.println("Processed log hash: " + processedHash);
//    }
}
