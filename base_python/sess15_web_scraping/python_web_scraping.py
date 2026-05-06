# Python script to demonstrate scraping a website and storing the data to a file
# NB: Make sure you've installed requests and beautifulsoup4 modules: pip install requests beautifulsoup4
from importlib.metadata import files

# import the required modules
import requests
from bs4 import BeautifulSoup
import time
import csv
from pathlib import Path

# 1. Set up a polite user agent string
headers = {"User-Agent": "Edge (Windows NT 10.0; Win64; X64) MHD-Learning-Scraper/1.0"}

# 2. Specify the target URL (Website you wish to scrape)
url = "https://books.toscrape.com/"

# 3. Make the reques
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Request failed due to:\n{e}")
    exit(1)

# 4. Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# ----------------------------------------------------------------------------------------------------------------------
# 😊 Fun part now: Extract the data
# ----------------------------------------------------------------------------------------------------------------------

books = soup.find_all("h3")
prices = soup.find_all("p", class_="price_color")

# 5. Display the book titles then their prices
print("First 8 book title")
# for book in books[:8]:
# title = book.a["title"]
# print(f"* {title}")

print("First 8 book prices")
for price in prices[:8]:
    print(f"* {price.get_text().strip().replace('Â', '')}")

# 6. Combine the titles and prices safely
book_data = []
for book, price in zip(books, prices):
    title = book.find("a")["title"].strip()
    price_text = price.get_text().strip().replace("Â", "")
    book_data.append([title, price_text])

# ----------------------------------------------------------------------------------------------------------------------
# 7. 💾 Save the data to a CSV file
# ----------------------------------------------------------------------------------------------------------------------
# a. Build the path to the files folder where we'll save our scraped data
files_dir = Path.cwd().parent / "files"
files_dir.mkdir(exist_ok=True)

csv_path = files_dir / "scraped_books.csv"
with open(csv_path, "w", newline="", encoding="utf-8-sig") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Price"])
    writer.writerows(book_data)
    print(book_data)

# Inform the user the data has been saved
print(f"Saved {len(book_data)} records to {csv_path}")
