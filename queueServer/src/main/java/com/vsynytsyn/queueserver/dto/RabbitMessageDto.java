package com.vsynytsyn.queueserver.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class RabbitMessageDto implements Serializable {
    private String hashValue;
    private String message;
    private String timestamp;
}
