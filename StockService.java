package com.trademind.service;

import org.springframework.stereotype.Service;

import com.trademind.dto.MarketQuote;
import com.trademind.model.Stock;

@Service
public class StockService {

	private final MarketDataService marketDataService;

	public StockService(MarketDataService marketDataService) {
		this.marketDataService = marketDataService;
	}

	public Stock getStock(String ticker) {

		MarketQuote quote = marketDataService.getQuote(ticker);

		String signal;

		if (quote.getD() > 0) {
			signal = "BUY";
		} else if (quote.getD() < 0) {
			signal = "SELL";
		} else {
			signal = "HOLD";
		}

		return new Stock(ticker.toUpperCase(), ticker.toUpperCase(), quote.getC(), quote.getD(), signal);

	}

}
