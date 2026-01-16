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
