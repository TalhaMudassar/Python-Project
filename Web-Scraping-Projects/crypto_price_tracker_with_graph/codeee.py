"""
 Challenge: Crypto Price Tracker with Graphs

Goal:
- Fetch live prices of the top 10 cryptocurrencies using CoinGecko's free public API
- Store prices in a CSV file with timestamp
- Generate a line graph for a selected coin over time (price vs. time)
- Repeatable — user can run this multiple times to log data over time

JSON handling, API usage, CSV storage, matplotlib graphing
"""

import os
import csv
from datetime import datetime
import requests
import matplotlib.pyplot as plt

# API 
API_URL = "https://api.coingecko.com/api/v3/coins/markets"

# Parameters for API request (Top 10 coins by market cap in USD)
PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',  
    'per_page': 10,
    'page': 1,
    'sparkline': False
}

# CSV file name to store fetched crypto data
CSV_FILE = 'crypto_prices.csv'   


def fetch_crypto_data():
    """Fetch live cryptocurrency data using CoinGecko API."""
    response = requests.get(API_URL, params=PARAMS)
    return response.json()


def save_to_csv(data):
    """Append fetched crypto data into a CSV file with a timestamp."""
    file_exists = os.path.isfile(CSV_FILE)

    # Open the CSV file in append mode
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)

        # If file doesn't exist, write the header row
        if not file_exists:
            writer.writerow(["timestamp", "coin", "price"])

        # Current timestamp for each fetch
        timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S") 

        # Write each coin's data into the CSV
        for coin in data:
            writer.writerow([timestamp, coin["id"], coin['current_price']])

    print("✅ Data saved to CSV")


def plot_graph(coin_id):
    """Plot price vs time graph for the selected coin using matplotlib."""
    times = []
    prices = []

    # Read CSV and filter rows for the selected coin
    with open(CSV_FILE, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["coin"] == coin_id:
                times.append(row['timestamp'])
                prices.append(float(row['price']))

    # If no data found for the given coin
    if not times:
        print(f"No data found for {coin_id}")
        return

    # Plot line graph
    plt.figure(figsize=(10, 5))
    plt.plot(times, prices, marker='o')
    plt.title(f"Price Trend for {coin_id}")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    plt.show()


def main():
    """Main function to fetch, save, display, and plot crypto prices."""
    print("Fetching live crypto data...")
    crypto_data = fetch_crypto_data()
    save_to_csv(crypto_data)

    # Print fetched coins with prices
    print("-" * 30)
    for coin in crypto_data:
        print(f"{coin['id']} - $ {coin['current_price']}")
    print("-" * 30)

    # Ask user to enter a coin name to plot graph
    choice = input("Enter the coin name to get graph: ").strip().lower()
    if choice:
        plot_graph(choice)


# Entry point
if __name__ == "__main__":
    main()
