from typing import TypedDict


class ProductRecord(TypedDict):
    product_id: str
    title: str
    price: str
    rating: int
    image_url: str
    image_path: str
    source: str