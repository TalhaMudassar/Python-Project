import requests
from bs4 import BeautifulSoup
import csv

URL = "http://www.amis.pk/daily%20market%20changes.aspx"
CSV_FILE = "amis_daily_prices.csv"

def fetch_daily_prices():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(URL, headers=headers, timeout=15)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Failed to fetch the page: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # Locate the table by ID
    table = soup.find("table", {"id": "ctl00_cphPage_GridView1"})
    if not table:
        print("❌ Could not find the data table on the page.")
        return []

    rows = table.find_all("tr")[1:]  # skip the header row
    data = []

    for row in rows:
        cols = [col.get_text(strip=True) for col in row.find_all(["td", "th"])]
        if len(cols) >= 5:
            city = cols[0]
            crop = cols[1]
            todays_price = cols[2]
            yesterdays_price = cols[3]
            price_change = cols[4]
            price_direction = cols[5] if len(cols) > 5 else ""
            data.append([city, crop, todays_price, yesterdays_price, price_change, price_direction])

    return data


def save_to_csv(data):
    if not data:
        print("⚠ No data to save.")
        return

    headers = ["City", "Crop", "Today's Price", "Yesterday's Price", "Change", "Direction"]

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

    print(f"✅ Data saved to {CSV_FILE}")


def main():
    print("📡 Fetching daily market prices from AMIS...")
    data = fetch_daily_prices()
    print(f"📊 Total records fetched: {len(data)}")
    save_to_csv(data)


if __name__ == "__main__":
    main()
