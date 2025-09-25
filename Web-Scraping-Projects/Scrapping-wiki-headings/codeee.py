"""
 Challenge: Scrape Wikipedia h2 Headers

Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python (programming language).

Your task is to:
1. Download the HTML of the page.
2. Parse all <h2> section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Bonus:
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.
"""

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

def get_h2_headers(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}  # prevent blocking
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page:\n{e}")
        return []

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")
    print(h2_tags)

    # Extract clean text without [edit]
    headers = []
    for tag in h2_tags:
        text = tag.get_text(strip=True).replace("[edit]", "")
        headers.append(text)

    # Output results
    print(f"Total <h2> headers found: {len(headers)}")
    print("First 10 headers:")
    for h in headers[:10]:
        print("-", h)

    return headers

 
if __name__ == "__main__":
    get_h2_headers(URL)
