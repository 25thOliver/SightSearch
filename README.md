# SightSearch

**SightSearch** is a robust, scalable data ingestion pipeline designed to scrape product data, process product images, and store structured metadata for downstream search and analysis applications.

Built with **Apache Airflow**, **Docker**, and **Python**, SightSearch orchestrates the entire lifecycle of data ingestion, from web scraping to database storage, ensuring reliability and ease of monitoring.

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

## Usage

1.  **Trigger the Pipeline**:
    - In the Airflow UI, find the DAG named `sightsearch_ingestion_pipeline`.
    - Toggle the switch to **Unpause** the DAG.
    - Click the **Play** button (Trigger DAG) to start a manual run.

2.  **Monitor Progress**:
    - Click on the DAG ID to view the Grid/Graph view.
    - Watch as tasks (`scrape`, `image_processing`, `validate`, `store_valid`) turn dark green (success).

3.  **Verify Data**:
    - You can connect to the MongoDB instance on port `27020` to inspect the ingested data in the `sightsearch.products` collection.

---

## Project Structure

```text
sightsearch/
├── docker/                 # Docker configuration files
│   ├── airflow/            # Airflow-specific Dockerfile and configs
│   │   └── dags/           # Airflow Directed Acyclic Graphs (DAGs)
│   ├── scraper/            # Scraper-specific Dockerfile
│   ├── docker-compose.yml  # Service orchestration
│   └── .env                # (Created by you) Secrets and env vars
├── src/                    # Application source code
│   ├── scraper.py          # Web scraping logic
│   ├── image_processing.py # Image metadata extraction
│   ├── storage.py          # Database interactions
│   └── validators.py       # Data validation logic
├── tests/                  # Unit tests
├── images/                 # Downloaded product images
├── requirements.airflow.txt # Python dependencies for Airflow
└── README.md               # This file
```

---

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features:

1.  Fork the repository.
2.  Create a feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

---
