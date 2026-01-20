from typing import Dict, Tuple
from datetime import datetime
import re

from src.models import ProductRecord
REQUIRED_FIELDS = {
    "product_id",
    "title",
    "image_path",
    "image_url",
    "price",
    "rating",
    "source",
}

def validate_product(record: Dict) -> Tuple[bool, Dict]:
    """
    Validates and normalizes a product record.
    Returns (is_valid, cleaned_record)
    """

    missing = REQUIRED_FIELDS - record.keys()
    if missing:
        return False, {"error": f"Missing fields: {missing}"}
    
    if not record["image_path"]:
        return False, {"error": "Missing image_path"}
    
    # Normalize price (strip weird encoding, keep numeric)
    raw_price = record["price"]

    # Extract numeric value safely
    match = re.search(r"([\d]+(?:\.\d+)?)", raw_price)
    if not match:
        return False, {"error": f"Invalid price: {raw_price}"}
    
    record["price"] = float(match.group(1))
    
    # Enforce rating range
    if not (1 <= record["rating"] <= 5):
        return False, {"error": f"Invalid rating: {record['rating']}"}
    
    record["validated_at"] = datetime.utcnow()

    return True, record