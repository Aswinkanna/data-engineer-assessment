# Work Log

## Day 0 – Clarify Questions & Pick Dataset
- Reviewed the assessment requirements and clarified open questions.
- Explored available GA4 datasets in BigQuery (`bigquery-public-data.ga4_obfuscated_sample_ecommerce`).
- Decided to use GA4 events export as the base dataset (`events_20210131`).
- Sketched a rough outline of the pipeline (staging → intermediate → marts → dashboard).
- Set up local development environment:
  - Python virtual environment
  - dbt project initialized
  - BigQuery connection tested with `dbt debug`

---

## Day 1 – Staging Models & Architecture
- Built **staging models**:
  - `stg_events.sql`: unified schema for historical + streaming data.
  - Added transformations: `event_date`, `event_timestamp (microseconds)`, `user_pseudo_id`, `event_name`, `traffic_source`.
- Created **schema tests**:
  - Non-null checks on  `event_timestamp`, `user_pseudo_id`.
  - Set up int_user_events model (deduplication).
  - Added tests for int_user_events (user_pseudo_id not null).
  
- Wrote **architecture documentation**:
  - Source → Staging → Intermediate → Marts → Dashboard.
  - Explained streaming ingestion flow vs. batch historical data.

---

## Day 2 – Attribution Models & Streaming Demo
- Implemented **intermediate layer**:
  - `int_user_events`: enriches events with derived timestamps and joins with user info.
- Built **mart models**:
  - `mart_first_click`: computes first-touch attribution per user.
  - `mart_last_click`: computes last-touch attribution per user.
- Set up **streaming demo**:
  - Python script (`stream_events.py`) to push new events into `events_stream`.
  - Validated integration by running `dbt run` and checking marts updated correctly.
- Debugged timestamp conversion issues (`TIMESTAMP_MICROS` vs INT64 microseconds).
- Confirmed end-to-end flow: new event → staging → marts.

---

## Day 3 – Dashboard & Submission
- Built **Streamlit dashboard (`dashboard_app.py`)**:
  - Live event viewer (last 10 streamed events).
  - Attribution summary charts (first-touch / last-touch sources).
- Polished **README**:
  - Setup instructions
  - Architecture diagram
  - Usage flow: `stream_events.py → dbt run → streamlit run`
- Added **automation script (`pipeline_runner.py`)** to orchestrate:
  1. Streaming events
  2. dbt transformations
  3. Dashboard launch
- Recorded demo walkthrough video.
- Final submission prepared.

---
