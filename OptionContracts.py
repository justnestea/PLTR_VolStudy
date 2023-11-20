from polygon.rest import RESTClient
from polygon.rest.models.request import RequestOptionBuilder
import pandas_market_calendars as mcal
import pandas as pd
import json
import time

# API Key 
with open('/Users/jimenanestares/Desktop/p1/polygonAPIKey', 'r') as file:
    apiKey = file.read().strip()

client = RESTClient(api_key = apiKey)

# Create list of market dates
nyse = mcal.get_calendar('NYSE')
early = nyse.schedule(start_date='2022-10-13', end_date='2023-10-13')
check = mcal.date_range(early, frequency='1D')

dateList = []
for i in check:
    dateList.append(i.date().strftime('%Y-%m-%d'))

# List of Parameters for the call 
ticker = "PLTR"
contractTypes = ["call", "put"]
expiration = ["true", "false"]
limit = 1000
sort = "expiration_date"
order = "asc"
rate_limit = 30  # seconds in between api calls 

# Body of API Calll 

# FIRST LOOP OVER EXPIRATION
for ex in expiration:
    for c in contractTypes:
        for d in dateList:
            # List of responses 
            api_responses = []
            # Make the API request
            request = client.list_options_contracts(
                underlying_ticker = ticker, 
                contract_type = c,
                as_of = d,
                expired = ex,
                limit = limit,
                sort = sort,
                order = order,
                )
            # Make list to append API responses

            try: 
                for r in request:
                    # create the output JSON format
                    js = {"additional_underlyings": r.additional_underlyings,
                            "cfi": r.cfi,
                            "contract_tye": r.contract_type,
                            "correction": r.correction,
                            "exercise_style": r.exercise_style,
                            "expiration_date": r.expiration_date,
                            "primary_exchange": r.primary_exchange,
                            "shares_per_contract": r.shares_per_contract,
                            "strike_price": r.strike_price,
                            "ticker": r.ticker,
                            "underlying_ticker": r.underlying_ticker
                    }
                    
                    # append the response
                    api_responses.append(js)
                # Save the succesful calls to a JSON file with a name detailing the date, expiration, and contract type
                with open(f'/Users/jimenanestares/Desktop/p1/options_api_responses/response_{d}_{c}.json', 'w') as json_file:
                    json.dump(api_responses, json_file, indent=4)

            except Exception as e:
                # append the response with the exception
                with open('/Users/jimenanestares/Desktop/p1/options_api_responses/failures_log.txt','a') as failures:
                    entry = f"{d},{e}\n"
                    failures.write(entry)

            print(f'Response for Date: {d} saved')

            # Sleep to enforce the rate limit
            time.sleep(rate_limit)

    print("All API calls completed.")
    