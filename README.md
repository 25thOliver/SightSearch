# SightSearch

**SightSearch** is a robust, scalable data ingestion pipeline designed to scrape product data, process product images, and store structured metadata for downstream search and analysis applications.

Built with **Apache Airflow**, **Docker**, and **Python**, SightSearch orchestrates the entire lifecycle of data ingestion—from web scraping to database storage—ensuring reliability and ease of monitoring.

---

## Features

- **Automated Scraping**: Fetches product data (titles, prices, ratings) from target websites.
- **Image Processing**: Downloads and extracts metadata (dimensions, format, pHash) from product images.
- **Data Validation**: Ensures data integrity with strict schema validation before storage.
- **Orchestration**: Fully containerized Airflow pipeline for scheduling and monitoring tasks.
- **Scalable Storage**:
    - **MongoDB**: Stores flexible product metadata and rejected records.
    - **PostgreSQL**: Manages Airflow's internal state.

---