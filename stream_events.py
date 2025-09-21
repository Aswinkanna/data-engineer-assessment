from google.cloud import bigquery
import time

client = bigquery.Client()

# Destination BigQuery table
table_id = "dbtproject-395506.ga4_demo.events_stream"

#STREAMING cannot be done in bigquery free version
# Example event payload
# rows_to_insert = [
#     {
#         "event_date": "2025-09-19",   # YYYYMMDD
#         "event_timestamp": int(time.time() * 1e6),  # microseconds
#         "user_pseudo_id": "user1",
#         "event_name": "page_view",
#         "source": "google",
#         "medium": "cpc"
#     }
# ]

# Insert into BigQuery
# errors = client.insert_rows_json(table_id, rows_to_insert)
# if errors:
#     print("Errors:", errors)
# else:
#     print("Inserted rows successfully")


job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
)

with open("events.json", "rb") as source_file:
    load_job = client.load_table_from_file(source_file, table_id, job_config=job_config)

load_job.result()  # Wait for job to finish

print(f"Loaded {load_job.output_rows} rows into {table_id}")