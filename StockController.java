package com.trademind.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.trademind.model.Stock;
import com.trademind.service.StockService;

@RestController
public class StockController {

    private final StockService stockService;
   
    public StockController(StockService stockService) {
        this.stockService = stockService;
    }

    @GetMapping("/stock/{ticker}")
    public Stock getStock(@PathVariable String ticker) {
        return stockService.getStock(ticker);
    }

}
