package com.vsynytsyn.queueserver.service;

import com.vsynytsyn.queueserver.config.RabbitMQConfig;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.stereotype.Service;

@Service
public class LogProcessingService {
    private final RabbitTemplate rabbitTemplate;

    public LogProcessingService(RabbitTemplate rabbitTemplate) {
        this.rabbitTemplate = rabbitTemplate;
    }


    public void processLog(String hash, String message, String timestamp, LogLevels logLevel) {
        System.out.printf("Received log (%s): [%s] %s '%s'\n", hash, logLevel, timestamp, message);
        addLogToProcessedQueue(hash);
    }

    private void addLogToProcessedQueue(String originalHash) {
        rabbitTemplate.convertAndSend(
                RabbitMQConfig.PROCESSED_EXCHANGE_NAME,
                RabbitMQConfig.ROUTING_KEYS.LogProcessed.routingKey,
                originalHash
        );
//        System.out.println("Log added to processed queue.");
    }

    public enum LogLevels {
        DEBUG,
        INFO
    }
}
