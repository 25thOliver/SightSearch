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