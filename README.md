# BTC-USD-data-gathering

This repository contains a CSV file with **Bitcoin OHLC hourly data** covering the period from **2015-01-01 to sept-2025**.  

## Source  
Data was originally obtained from Kaggle:  
[Bitcoin Historical Data (mczielinski)](https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data)  

This Kaggle dataset itself was scraped from the **Bitstamp API**, which provides minute-level OHLCV data.  

## Dataset Details  
- **Format**: CSV  
- **Fields**: Open, High, Low, Close, Volume, Timestamp  
- **Granularity**: 1-hour candles  

# BTC-USD-data-gathering
#
# This repository contains a CSV file with Bitcoin OHLC hourly data
# covering the period from 2015-01-01 to Sept-2025.
#
# Source: Kaggle: https://www.kaggle.com/mczielinski/bitcoin-historical-data
#         (scraped from the Bitstamp API)
#
# Dataset Details:
# - Format: CSV
# - Fields: Open, High, Low, Close, Volume, Timestamp
# - Granularity: 1-hour candles
#
# Data Cleaning
#
# A cleaning script data_cleaning.py is included to prepare the data:
# - Handle missing values
# - Remove duplicate timestamps
# - Sanity check for outliers
# - Set datetime index and sort chronologically
#
# The cleaned data is saved as btc_1h_cleaned.csv and is ready for analysis.
#
# Usage:
#
# Run the cleaning script:
# $ python data_cleaning.py
#
# Output: btc_1h_cleaned.csv
