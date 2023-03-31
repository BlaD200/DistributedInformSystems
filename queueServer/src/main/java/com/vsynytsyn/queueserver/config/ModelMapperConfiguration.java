package com.vsynytsyn.queueserver.config;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ModelMapperConfiguration {

    @Bean
    public ObjectMapper mapper() {
        return new ObjectMapper();
    }

//    @Bean
//    public ModelMapper modelMapper(){
//        ModelMapper modelMapper = new ModelMapper();
//        modelMapper.getConfiguration()
//                .setFieldMatchingEnabled(true)
//                .setMatchingStrategy(MatchingStrategies.STRICT)
//                .setFieldAccessLevel(PRIVATE)
//                .setSkipNullEnabled(true);
//        return modelMapper;
//    }
}
