import lxml
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


response = requests.get(BASE_URL, headers=HEADERS)
amazon_response = response.text

soup = BeautifulSoup(amazon_response, "lxml")


def get_title(soup):
    product_title = soup.find(name="span", id="productTitle").getText().strip()
    return f"Product title: {product_title}"


def get_price(soup):
    product_price = soup.find(
        name="span", class_="a-price-whole").getText().strip()
    return f"Product price: ${product_price}"


def get_ratings(soup):
    product_rating = soup.find(
        name="span", class_="a-icon-alt").getText().strip()
    return f"Product rating: {product_rating}"


print(get_title(soup))
print(get_price(soup))
print(get_ratings(soup))
