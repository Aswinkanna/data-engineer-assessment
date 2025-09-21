# data-engineer-assessment

## Overview
This project demonstrates a GA4 data pipeline using Python, dbt, and Streamlit. It includes:

- Streaming GA4 events to BigQuery  
- Running dbt models for staging and attribution  
- Interactive Streamlit dashboard  
- Full pipeline automation via `pipeline_runner.py`

1. Install Google Cloud SDK:  
   ```bash
   curl https://sdk.cloud.google.com | bash
   exec -l $SHELL
   gcloud init

   Authenticate application default credentials:

   gcloud auth application-default login
   gcloud config set project <YOUR_PROJECT_ID>

2. Install Dependencies

    Install Python packages from requirements.txt:

    pip install -r requirements.txt


    requirements.txt includes:

    google-cloud-bigquery==3.10.0
    dbt-bigquery==1.6.0
    streamlit==1.27.0
    pandas==2.1.0
    numpy==1.26.0

3. Run Full Pipeline

    Run the pipeline script to execute all steps sequentially:

    python python/pipeline_runner.py

    This script performs:
        Streams events to BigQuery (stream_events.py)
        Executes dbt models (dbt run)
        Starts the Streamlit dashboard (dashboard_app.py)

    Features:
        - Full automation from event ingestion to dashboard
        - Real-time streaming simulation
        - Interactive dashboard with key metrics