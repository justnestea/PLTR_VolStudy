import pandas as pd
import json
import time
import pathlib
import re
from polygon.rest import RESTClient
import pandas_market_calendars as mcal


# API Key 
with open('/Users/jimenanestares/Desktop/p1/polygonAPIKey', 'r') as file:
    apiKey = file.read().strip()

client = RESTClient(api_key = apiKey)

# Import the file with the option contracts
directory_path = pathlib.Path("/Users/jimenanestares/Desktop/p1/options_api_responses")
optcont_filename = "OptionContractsNoDupes.csv"
option_contracts = pd.read_csv(f'{directory_path}/{optcont_filename}')

# Create list of historical dates to query (market dates)
nyse = mcal.get_calendar('NYSE')
early = nyse.schedule(start_date='2022-10-13', end_date='2023-10-13')
check = mcal.date_range(early, frequency='1D')
dateList = []
for i in check:
    dateList.append(i.date().strftime('%Y-%m-%d'))

# Create file for failed api calls
log_file = open("api_failures.txt", "a")

# Time limit on API calls
rate_limit = 15

# List of tickers from the dataset
tick = option_contracts["ticker"]

# Loop for API
for t in tick:
    for d in dateList:
        try:
            request = client.get_daily_open_close_agg(
                ticker= tick,
                date= dt,
                )
            
            if request.status == 200:
                for r in request:
                    data = {
                        "afterHours": r.afterHours,
                        "close": r.close,
                        "from": r.from_,
                        "high": r.high,
                        "low": r.low,
                        "open": r.open,
                        "preMarket": r.preMarket,
                        "status": r.status,
                        "symbol": r.symbol,
                        "volume": r.volume
                        }
                    # convert to json data
                    json_data = json.dumps(data, indent=4)  # The `indent` parameter is used for pretty printing
                    # write to json 
                    with open(f'{directory_path}/{d}_{t}', "w") as json_file:
                        json_file.write(json_data)
        except:
                with open('/Users/jimenanestares/Desktop/p1/options_api_responses/daily_api_failures.txt','a') as failures:
                    entry = f'{d}_{t}\n'
                    failures.write(entry)

        print(f'Response for Date: {d} saved')
        # Sleep to enforce the rate limit
        time.sleep(rate_limit)