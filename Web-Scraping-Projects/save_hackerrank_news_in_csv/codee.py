"""
 Challenge: Hacker News Top Posts Scraper

Build a Python script that:
1. Fetches the HN homepage (news.ycombinator.com).
2. Extracts the top 20 post titles and URLs.
3. Saves the results into a CSV file (`hn_top20.csv`) with columns:
   - Title
   - URL
4. Handles network errors and uses a clean CSV structure.
"""

import csv
import os 
import requests
from bs4 import BeautifulSoup

URL = 'https://news.ycombinator.com/'
CSV_FILE = 'data.csv'

def fetch_top_post():
    try:
        response = requests.get(URL,timeout=10)
        response.raise_for_status()
    except requests.RequestException as e :
        print(f" Network error \n {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    post_link = soup.select("span.titleline > a")
    
    
    posts = []
    for link in post_link[:10]:
        title = link.text.strip()
        url = link.get("href").strip()
        posts.append({'title':title,'url':url})
        # print(f"{title} \n {url}  \n\n")
    return posts


def save_to_csv(posts):
    if not posts:
        print('Noting to save ')
        return
    
    with open(CSV_FILE,'w',newline="",encoding='utf-8') as file :
        writer = csv.DictWriter(file,fieldnames=["title","url"])
        writer.writeheader()
        writer.writerows(posts)
        print(f"saved hacker news  to {CSV_FILE}")
        
    
        
def main():
    print("Scrapping th HN News")
    posts = fetch_top_post()
    print("Collection All Data .... ")
    save_to_csv(posts)
    
    
if __name__ == '__main__':
    main()
        