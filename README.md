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

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **[Docker](https://docs.docker.com/get-docker/)**: For running the containerized services.
- **[Docker Compose](https://docs.docker.com/compose/install/)**: For orchestration of the multi-container environment.

---

## Getting Started

Follow these steps to get the pipeline up and running in minutes.

### 1. Clone the Repository

```bash
git clone https://github.com/25thOliver/SightSearch.git
cd SightSearch
```

### 2. Configure Environment Variables

For security, the project uses a `.env` file to manage sensitive credentials.

1.  Navigate to the `docker` directory:
    ```bash
    cd docker
    ```
2.  Create a file named `.env` and add the following configuration. You can change the passwords for a production setup:

    ```ini
    # Database Configuration
    POSTGRES_USER=airflow
    POSTGRES_PASSWORD=airflow
    POSTGRES_DB=airflow

    # MongoDB
    MONGO_URI=mongodb://mongodb:27017
    MONGO_DB=sightsearch

    # Airflow Admin
    AIRFLOW_ADMIN_USER=admin
    AIRFLOW_ADMIN_PASSWORD=admin
    AIRFLOW_ADMIN_EMAIL=admin@example.com

    # Airflow Core
    AIRFLOW__CORE__EXECUTOR=LocalExecutor
    ```

### 3. Start the Services

From the `docker` directory, start the entire stack using Docker Compose:

```bash
docker-compose up -d --build
```

This command will:
- Build the custom Airflow and Scraper images.
- Start MongoDB, PostgreSQL, and Airflow services.
- Initialize the Airflow database and create the admin user.

### 4. Access the Application

Once the services are running (wait a minute or two for initialization):

- **Airflow UI**: Open [http://localhost:8080](http://localhost:8080) in your browser.
    - **Username**: `admin` (or what you set in `.env`)
    - **Password**: `admin`

---