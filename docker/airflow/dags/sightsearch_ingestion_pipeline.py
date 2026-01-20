from datetime import datetime
from airflow import DAG
from airflow.decorators import task
 
# Import  pipeline task functions
from src.scraper import scrape_catalogue
from src.image_processing import extract_image_metadata
from src.validators import validate_product
from src.storage import upsert_product, insert_rejected

DEFAULT_ARGS = {
    "owner": "sightsearch",
    "retries": 2,
}

with DAG(
    dag_id="sightsearch_ingestion_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args=DEFAULT_ARGS,
    tags=["sightsearch", "data-engineering"],
) as dag:
    
    @task
    def scrape():
        return scrape_catalogue(max_pages=2)
    
    @task
    def image_processing(products):
        enriched = []
        for p in products:
            try:
                meta = extract_image_metadata(p["image_path"])
                p.update(meta)
            except Exception as e:
                p["image_metadata_error"] = str(e)
            enriched.append(p)
        return enriched
    
    @task
    def validate(products):
        valid, rejected = validate_product(products)
        return {
            "valid": valid,
            "rejected": rejected,
        }

    @task
    def store_valid(payload):
        upsert_product(payload["valid"])

    @task
    def store_rejected(payload):
        upsert_rejected(payload["rejected"])

    scraped = scrape()
    processed = image_processing(scraped)
    validated = validate(processed)

    store_valid(validated)
    store_rejected(validated)