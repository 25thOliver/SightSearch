FROM apache/airflow:3.1.6

USER airflow

# Copy requirements file
COPY requirements.airflow.txt /tmp/requirements.airflow.txt

# Install all dependencies
RUN pip install --no-cache-dir apache-airflow-providers-fab && \
    pip install --no-cache-dir -r /tmp/requirements.airflow.txt
