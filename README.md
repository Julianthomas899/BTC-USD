# BTC-USD-data-gathering

This repository contains a CSV file with **Bitcoin OHLC hourly data** covering the period from **2015-01-01 to mid-2025**.  

## Source  
Data was originally obtained from Kaggle:  
[Bitcoin Historical Data (mczielinski)](https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data)  

This Kaggle dataset itself was scraped from the **Bitstamp API**, which provides minute-level OHLCV data.  

## Dataset Details  
- **Format**: CSV  
- **Fields**: Open, High, Low, Close, Volume, Timestamp  
- **Granularity**: 1-hour candles  

## Data Cleaning Steps  
1. Removed all data prior to **2015-01-01**.  
2. Resampled minute-level data into **hourly intervals** by taking the **first minute of each hour** as the OHLC value.  
