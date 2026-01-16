from typing import Dict, Tuple
from datetime import datetime

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
    price = record["price"]
    price = price.replace("A", "").replace("£", "").strip()

    try:
        record["price"] = float(price)
    except ValueError:
        return False, {"error": f"Invalid price: {record['price']}"}
    
    # Enforce rating r