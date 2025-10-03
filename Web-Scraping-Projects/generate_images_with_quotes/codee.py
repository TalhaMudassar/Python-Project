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
from PIL import Image, ImageDraw, ImageFont


BASE_URL = "https://quotes.toscrape.com/"


OUTPUT_DIR = "quotes"


def fetch_quotes():
    """Fetch the first 5 quotes (text + author) from the website."""
    response = requests.get(BASE_URL)  # Send GET request to the website
    soup = BeautifulSoup(response.text, "html.parser")  # Parse HTML
    quotes = soup.select("div.quote")  # Select all divs containing quotes

    quotes_data = []

    # Loop through the first 5 quotes and extract text + author
    for q in quotes[:5]:
        text = q.find("span", class_="text").text.strip("“”")
        author = q.find("small", class_="author").text
        quotes_data.append((text, author))

    # ✅ Return AFTER collecting all quotes (indentation was wrong before)
    return quotes_data


def create_image(text, author, index):
    """Create an image for a given quote and save it to the output folder."""
    width, height = 800, 400
    background_color = "#f7e3af"  # Light background color
    text_color = "#232323"       # Dark text color

    # Create a new blank image
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Load default fonts (can be replaced with custom fonts if needed)
    font = ImageFont.load_default()
    author_font = ImageFont.load_default()

    # Wrap quote text to fit within the image width
    wrapped = textwrap.fill(text, width=60)
    author_text = f"_ {author}"  # Author name format

    # Draw quote text
    y_text = 60
    draw.text((40, y_text), wrapped, font=font, fill=text_color)

    # Adjust Y position for author line
    y_text += wrapped.count('\n') * 15 + 40

    # Draw author text
    draw.text((500, y_text), author_text, font=author_font, fill=text_color)

    # Create output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Save the generated image
    file_name = os.path.join(OUTPUT_DIR, f"quote_{index+1}.png")
    image.save(file_name)
    print(f"✅ saved: {file_name}")


def main():
    quotes = fetch_quotes()
    for idx, (text, author) in enumerate(quotes):
        create_image(text, author, idx)


# Entry point
if __name__ == "__main__":
    main()
