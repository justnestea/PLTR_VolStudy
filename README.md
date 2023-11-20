# PLTR Volatility Study
## Abstract
- **Objective**: Learn about option contracts by: - Determine how accurate the market is at predicting the volatility of PLTR stock prices at a given time (t) as reflected in option contract prices. 
- Create a strategies that could exploit with mismatches in volatility predictions.
- Backtest strategies to simulate their performance
- **Methods**: 
    1. Calculate Actual Volatility (Historical Volatility) of PLTR stock prices by:
        1.  Gathering historical PLTR stock prices over 4 years from Yahoo Finance 
        2. Calculating the actual volatility using 2 methods: 
            - Standard Deviations of Logarithmic Returns
            - Standard Deviation of Exponentially Weighted Moving Averages
    2. Calculate Implied Volatility (Future Market Expectations on Volatility) of PLTR stock prices by:
        1. Gathering all listed option contracts over 3 years from Polygon.io's *OptionContracts* API.
        2. Deducing from the above dataset that:
        ''
        issue date =  (first time it appears listed) 
        ''
        3. Gathering historical daily prices for each option contract from their issue date to the expiration date. Studying the ThetaData API library.
            > Assume that the contract was exercised if no data is available for a continuous period period before and ending on the expiration date. 
        3. Gathering historical interest rates over 3 years.
        4. Noting that Palantir has not issued dividends or stock splits since going public.
        5. Calculate the implied volatility using Binomial Option Pricing Model and considering complementing with other pricing methods.
    3. For each day t since PLTR went public, compare the implied volatility at t with the actual volatility at t+1: 
     - (for each option contract?) - likely too much data
     - (for each grouping of strike prices ?) 
        - (for each option contract type) 
    4. Learn more about options tradings strategies. Come up with strategies for: 
    - Each contract type contracts with: 
        - IV > AV
        - IV < AV 
    5. Gather trade data and quote data for backtesting. (TBD)
    
