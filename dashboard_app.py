# dashboard_app.py
import streamlit as st
from google.cloud import bigquery
import pandas as pd
from datetime import datetime, timedelta

# Initialize BigQuery client
client = bigquery.Client(location="US")  # change if dataset is in a different location

st.title("GA4 Attribution Dashboard (First vs Last Click)")

# Helper: convert microseconds to datetime.date
def micros_to_date(series):
    return pd.to_datetime(series, unit='us').dt.date

# 1️⃣ First vs Last Totals
st.header("First vs Last Click Totals")
query_totals = """
SELECT COUNT(DISTINCT user_pseudo_id) AS user_count
FROM `dbtproject-395506.ga4_demo_marts.mart_first_click`
UNION ALL
SELECT COUNT(DISTINCT user_pseudo_id) AS user_count
FROM `dbtproject-395506.ga4_demo_marts.mart_last_click`
"""
totals = client.query(query_totals).to_dataframe()
totals['attribution_type'] = ['First', 'Last']
st.bar_chart(totals.set_index('attribution_type'))

# 2️⃣ 14-Day User Time Series (First Click)
st.header("14-Day User Time Series")
query_first_click = """
SELECT first_event_time
FROM `dbtproject-395506.ga4_demo_marts.mart_first_click`
"""
df_first = client.query(query_first_click).to_dataframe()
# Convert microseconds to date
df_first['event_date'] = pd.to_datetime(df_first['first_event_time'], unit='us').dt.date

# Use max date in the dataset for 14-day window
max_date = df_first['event_date'].max()
df_last14 = df_first[df_first['event_date'] >= (max_date - pd.Timedelta(days=14))]

# Aggregate and plot
ts_counts = df_last14.groupby('event_date').size().reset_index(name='users')
ts_counts = ts_counts.sort_values('event_date')
st.line_chart(ts_counts.set_index('event_date'))


# 3️⃣ Channel Breakdown (Last Click)
st.header("Channel Breakdown")
query_channels = """
SELECT last_touch.source AS source,
       COUNT(DISTINCT user_pseudo_id) AS users
FROM `dbtproject-395506.ga4_demo_marts.mart_last_click`
GROUP BY source
ORDER BY users DESC
"""
channels = client.query(query_channels).to_dataframe()
st.bar_chart(channels.set_index('source'))

# 4️⃣ Live Panel: Recent Streamed Events
st.header("Live Streamed Events (Last 10)")
query_live = """
SELECT user_pseudo_id, event_name, event_timestamp
FROM `dbtproject-395506.ga4_demo_staging.stg_events`
ORDER BY event_timestamp DESC
LIMIT 10
"""
live_events = client.query(query_live).to_dataframe()
st.dataframe(live_events)

st.info("Dashboard updates automatically when you rerun or refresh Streamlit.")
