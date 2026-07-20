package com.trademind.model;

public class Stock {

    private String ticker;
    private String company;
    private double price;
    private double change;
    private String signal;

    public Stock() {
    }

    public Stock(String ticker,
                 String company,
                 double price,
                 double change,
                 String signal) {

        this.ticker = ticker;
        this.company = company;
        this.price = price;
        this.change = change;
        this.signal = signal;
    }

    public String getTicker() {
        return ticker;
    }

    public void setTicker(String ticker) {
        this.ticker = ticker;
    }

    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public double getChange() {
        return change;
    }

    public void setChange(double change) {
        this.change = change;
    }

    public String getSignal() {
        return signal;
    }

    public void setSignal(String signal) {
        this.signal = signal;
    }
}
