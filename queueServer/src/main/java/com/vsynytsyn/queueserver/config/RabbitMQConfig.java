package com.vsynytsyn.queueserver.config;

import org.springframework.amqp.core.*;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class RabbitMQConfig {
    public static final String PROCESSING_EXCHANGE_NAME = "LogProcessingExchange";
    public static final String PROCESSED_EXCHANGE_NAME = "LogProcessedExchange";


    @Bean
    public Queue logProcessingQueueDebug() {
        return QueueBuilder.durable(QueueNames.QueueDebug.queueName).build();
    }

    @Bean
    public Queue logProcessingQueueInfo() {
        return QueueBuilder.durable(QueueNames.QueueInfo.queueName).build();
    }

    @Bean
    public Queue logProcessedQueue() {
        return QueueBuilder.durable(QueueNames.QueueProcessed.queueName).build();
    }

    @Bean
    public Exchange logProcessingExchange() {
        return ExchangeBuilder
                .directExchange(PROCESSING_EXCHANGE_NAME)
                .durable(true)
                .build();
    }

    @Bean
    public Exchange logProcessedExchange() {
        return ExchangeBuilder
                .directExchange(PROCESSED_EXCHANGE_NAME)
                .durable(true)
                .build();
    }

    @Bean
    public Binding logProcessingBindingDebug() {
        return BindingBuilder
                .bind(logProcessingQueueDebug())
                .to(logProcessingExchange())
                .with(ROUTING_KEYS.LogDebug)
                .noargs();
    }

    @Bean
    public Binding logProcessingBindingInfo() {
        return BindingBuilder
                .bind(logProcessingQueueInfo())
                .to(logProcessingExchange())
                .with(ROUTING_KEYS.LogInfo)
                .noargs();
    }
    @Bean
    public Binding logProcessedBinding() {
        return BindingBuilder
                .bind(logProcessedQueue())
                .to(logProcessedExchange())
                .with(ROUTING_KEYS.LogProcessed)
                .noargs();
    }

    public enum ROUTING_KEYS {
        LogDebug("processLogDebug"),
        LogInfo("processLogInfo"),

        LogProcessed("processedLog");

        public final String routingKey;

        ROUTING_KEYS(String routingKey) {
            this.routingKey = routingKey;
        }
    }


    public enum QueueNames {
        QueueDebug("LogDebugProcessingQueue"),
        QueueInfo("LogInfoProcessingQueue"),

        QueueProcessed("LogProcessedQueue");

        public final String queueName;

        QueueNames(String queueName) {
            this.queueName = queueName;
        }
    }
}
