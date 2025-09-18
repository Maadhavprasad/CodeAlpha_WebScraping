import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL
url = "https://books.toscrape.com/catalogue/page-{}.html"

# Store scraped data
titles = []
prices = []
ratings = []

# Loop through first 5 pages
for page in range(1, 6):
    print(f"Scraping page {page}...")
    response = requests.get(url.format(page))
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        # Title
        title = book.h3.a["title"]
        titles.append(title)

        # Price
        price = book.find("p", class_="price_color").text
        prices.append(price)

        # Rating (convert class to readable format)
        rating_class = book.find("p", class_="star-rating")["class"]
        rating = rating_class[1]  # e.g., 'Three', 'Five'
        ratings.append(rating)

# Create DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating": ratings
})

# Save to CSV
df.to_csv("books_scraped_data.csv", index=False)
print("Scraping completed and saved to books_scraped_data.csv")
