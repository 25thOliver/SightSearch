import os
from pymongo import MongoClient
from pymongo.collection import Collection

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "sightsearch")

class MongoStorage:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DB]
        self.collection: Collection = self.db.products
        self.collection.create_index("product_id", unique=True)

    def upsert_product(self, record: dict) -> None:
        self.collection.update_one(
            {"product_id": record["product_id"]},
            {"$set": record},
            upsert=True,
        )
        print(f"[MongoDB] Upserted {record['product_id']}")