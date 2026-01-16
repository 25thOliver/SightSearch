import hashlib
import logging
import os
import time
from typing import Dict, Generator, List
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"
CATALOGUE_URL = urljoin(BASE_URL, "catalogue/")
IMAGE_DIR = os.getenv("IMAGE_DIR", "images")
REQUEST_TIMEOUT = 10
RATE_LIMIT_SECONDS = 1.0

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)

def _generate_product_id(title: str, price: str) -> str:
    raw = f"{title}-{price}".encode()
    return hashlib.sha256(raw).hexdigest()

def _download_image(image_url: str, product_id: str) -> str:
    os.makedirs(IMAGE_DIR, exist_ok=True)
    image_path = os.path.join(IMAGE_DIR, f"{product_id}.jpg")

    if os.path.exists(image_path):
        logger.info("Image exists, skipping downloading: %s", image_path)
        return image_path
    
    response = requests.get(image_url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()

    with open(image_path, "wb") as f:
        f.write(response.content)


    return image_path


def _parse_rating(tag) -> int:
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }
    classes = tag.get("class", [])
    for cls in classes:
        if cls in rating_map:
            return rating_map[cls]
    return 0


def scrape_page(page_url: str) -> List[Dict]:
    logger.info("Scraping page: %s", page_url)
    response = requests.get(page_url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    products = []

    for article in soup.select("article.product_pod"):
        title = article.h3.a["title"].strip()
        price = article.select_one(".price_color").text.strip()
        rating = _parse_rating(article.select_one(".star-rating"))

        image_rel_url = article.find("img")["src"]
        image_url = urljoin(page_url, image_rel_url)

        product_id = _generate_product_id(title, price)
        image_path = _download_image(image_url, product_id)

        products.append(
            {
                "product_id": product_id,
                "title": title,
                "price": price,
                "rating": rating,
                "image_url": image_url,
                "image_path": image_path,
                "source": "books_to_scrape",
            }        
        )

    return products


def scrape_catalogue(max_pages: int = 1) -> Generator[Dict, None, None]:
    next_page = "page-1.html"

    for _ in range(max_pages):
        page_url = urljoin(CATALOGUE_URL, next_page)
        products = scrape_page(page_url)

        for product in products:
            yield product

        soup = BeautifulSoup(
            requests.get(page_url, timeout=REQUEST_TIMEOUT).text,
            "html.parser",
        )
        next_button = soup.select_one("li.next a")

        if not next_button:
            break

        next_page = next_button("href")
        time.sleep(RATE_LIMIT_SECONDS)


if __name__ == "__main__":
    for record in scrape_catalogue(max_pages=2):
        logger.info("Scrapped product: %s", record["title"])