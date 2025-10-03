"""
 Challenge: Quote of the Day Image Maker

Goal:
- Scrape random quotes from https://quotes.toscrape.com/
- Extract quote text and author for the first 5 quotes
- Create an image for each quote using PIL
- Save images in 'quotes/' directory using filenames like quote_1.png, quote_2.png, etc.


"""
import os
import requests
import textwrap
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_DIR = "quotes" 


def fetch_quotes():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select("div.quote")
    
    quotes_data = []
    
    for q in quotes[:5]:
        text = q.find("span",class_="text").text.strip("“”") 
        author = q.find("small",class_="author").text
        
        quotes_data.append((text,author))
        return quotes_data
        
    