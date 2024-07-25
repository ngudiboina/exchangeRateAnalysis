import os
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import logging
import argparse
from datetime import datetime, timedelta
from cachetools import cached, TTLCache
##from dotenv import load_dotenv

# Setup logging
log_file = '/Users/pro/exchangeRateAnalysis/exchange_rate_analysis.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

# load_dotenv()

# Get the API key from the environment variable
# Not working, will fix later
# api_key = os.getenv('EXCHANGE_API_KEY')
# if not api_key:
#     raise ValueError("API key not found. Please set the EXCHANGE_API_KEY environment variable.")

base_url = 'https://api.exchangeratesapi.io/v1/'

## replace with original key
api_key = '<api_key>'


# Caching setup: cache results for 10 minutes
cache = TTLCache(maxsize=100, ttl=600)

# Define command-line arguments
parser = argparse.ArgumentParser(description='Fetch and analyze exchange rates.')
parser.add_argument('--base_currency', type=str, default='AUD', help='Base currency code')
parser.add_argument('--target_currency', type=str, default='NZD', help='Target currency code')
parser.add_argument('--days', type=int, default=30, help='Number of days to fetch data for')
args = parser.parse_args()

# Get the dates for the specified number of days
end_date = datetime.now()
start_date = end_date - timedelta(days=args.days)

# Format dates to match the API requirements (YYYY-MM-DD)
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')


# Function to fetch exchange rates with caching
@cached(cache)
def fetch_exchange_rates( api_key, start_date, end_date, base_currency, target_currency):
    url = f"{base_url}timeseries?access_key={api_key}&start_date={start_date}&end_date={end_date}&base={base_currency}&symbols={target_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


# Function to preprocess the data
def preprocess_data(data):
    if 'rates' not in data:
        raise ValueError("Missing 'rates' in response data")

    # Convert to pandas DataFrame
    rates = data['rates']
    df = pd.DataFrame(rates).T  # Transpose to have dates as rows

    # Rename the columns
    df.columns = ['ExchangeRate']

    # Ensure the index is a datetime type
    df.index = pd.to_datetime(df.index)

    # Sort by date
    df.sort_index(inplace=True)

    return df


# Fetch exchange rates
try:
    data = fetch_exchange_rates(api_key, start_date_str, end_date_str, args.base_currency, args.target_currency)
    df = preprocess_data(data)

    # Find the best and worst exchange rates
    best_rate_date = df['ExchangeRate'].idxmax()
    best_rate = df['ExchangeRate'].max()
    worst_rate_date = df['ExchangeRate'].idxmin()
    worst_rate = df['ExchangeRate'].min()

    # Calculate the average exchange rate for the month
    average_rate = df['ExchangeRate'].mean()

    # Convert DataFrame to JSON format
    json_output = df.to_json(orient='index', date_format='iso')
    print(json_output)

    # Print the best, worst, and average exchange rates
    print(f"Best exchange rate: {best_rate} on {best_rate_date.strftime('%Y-%m-%d')}")
    print(f"Worst exchange rate: {worst_rate} on {worst_rate_date.strftime('%Y-%m-%d')}")
    print(f"Average exchange rate for the past {args.days} days: {average_rate}")

    # Plot the exchange rates
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['ExchangeRate'], marker='o', linestyle='-', color='b')
    plt.title(f'Exchange Rates: {args.base_currency} to {args.target_currency} (Past {args.days} Days)')
    plt.xlabel('Date')
    plt.ylabel('Exchange Rate')
    plt.grid(True)
    plt.show()

except requests.HTTPError as http_err:
    logging.error(f"HTTP error occurred: {http_err}")
except requests.RequestException as req_err:
    logging.error(f"Request error occurred: {req_err}")
except ValueError as val_err:
    logging.error(f"Data processing error: {val_err}")
except Exception as err:
    logging.error(f"An error occurred: {err}")
