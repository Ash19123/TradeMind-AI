package com.trademind.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.trademind.dto.MarketQuote;

@Service
public class MarketDataService {

    private final RestTemplate restTemplate;

    @Value("${finnhub.api.key}")
    private String apiKey;

    @Value("${finnhub.base.url}")
    private String baseUrl;

    public MarketDataService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    public MarketQuote getQuote(String ticker) {

        String url = baseUrl
                + "/quote?symbol="
                + ticker
                + "&token="
                + apiKey;

        System.out.println("Calling API: " + url);

        return restTemplate.getForObject(url, MarketQuote.class);

    }

}
