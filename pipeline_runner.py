import subprocess
import sys

def run_step(command, description):
    """Run a shell command and wait until it finishes"""
    print(f"\n🚀 Starting: {description} ...\n")
    result = subprocess.run(command, shell=True)
    
    if result.returncode != 0:
        print(f"❌ Error in {description}. Exiting pipeline.")
        sys.exit(result.returncode)
    else:
        print(f"✅ Finished: {description}\n")


if __name__ == "__main__":
    # Step 1: Stream events into BigQuery
    run_step("python3 stream_events.py", "Streaming events to BigQuery")

    # Step 2: Run dbt models
    run_step("dbt run", "Running dbt transformations")

    # Step 3: Launch Streamlit dashboard
    print("\n📊 Launching Streamlit dashboard... (leave this running)")
    subprocess.run("streamlit run dashboard_app.py", shell=True)
