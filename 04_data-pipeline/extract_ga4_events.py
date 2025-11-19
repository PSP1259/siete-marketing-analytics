# GA4 Events Extraction Script
# This script reads cofiguration form config.yaml (config_example.yaml as fallback), authenticates against the GA4 Data API using a service account and exports specified events within a date range to CSV files.

import os # operating system functions
import yaml # YAML file parsing
import pandas as pd # row and column data manipulation csv export

from google.analytics.data_v1beta import BetaAnalyticsDataClient # GA4 Data API client library
from google.analytics.data_v1beta.types import ( # request-object types to the GA4 Data API
    RunReportRequest,
    DateRange,
    Metric,
    Dimension,
    Filter,
    FilterExpression, 
)
from google.oauth2 import service_account  # service account authentication

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # base directory of the script, advantage: works independent of the current working directory


def load_config(): # load configuration from config.yaml or config_example.yaml
    if os.path.exists(os.path.join(BASE_DIR, "config.yaml")):
        config_path = os.path.join(BASE_DIR, "config.yaml")
    else:
        config_path = os.path.join(BASE_DIR, "config_example.yaml") # fallback for repositories git-ignored config.yaml

    with open(config_path, "r", encoding="utf-8") as f: # open and read the config file
        return yaml.safe_load(f)


def get_client(key_file): # authenticate against GA4 Data API using service account key file
    credentials = service_account.Credentials.from_service_account_file(key_file) # load service account credentials from JSON key file
    return BetaAnalyticsDataClient(credentials=credentials) # create GA4 Data API client with the loaded credentials


def fetch_event_report(client, property_id, event_name, start_date, end_date): # replace hard-coded event report with dynamic event name
    request = RunReportRequest(
        property=f"properties/{property_id}",
        metrics=[Metric(name="eventCount")], # how many times the event occurred
        dimensions=[
            Dimension(name="date"),   # when the event occurred
            Dimension(name="itemName"), # product name
            Dimension(name="eventName"), # GA4 event name
        ],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        dimension_filter=FilterExpression(
            filter=Filter(
                field_name="eventName",
                string_filter=Filter.StringFilter(value=event_name),
            )
        ),
    )
    return client.run_report(request) # execute the report request and return the response


def save_report_to_csv(report, event_name, output_folder): # Convert GA4 API response rows into a structured DataFrame and export to CSV
    rows = []
    for row in report.rows:
        rows.append(
            {
                "date": row.dimension_values[0].value,
                "item_name": row.dimension_values[1].value,
                "event_name": row.dimension_values[2].value,
                "event_count": int(row.metric_values[0].value),
            }
        )

    os.makedirs(output_folder, exist_ok=True) # # Ensure output folder exists
    output_path = os.path.join(output_folder, f"{event_name}.csv") # Create file path (e.g. data/view_item.csv)
    df = pd.DataFrame(rows)
    df.to_csv(output_path, index=False)
    print(f"Exported: {output_path}")


def main(): 
    # Main pipeline execution: 1. Load config, 2. Create GA4 API client, 3. Loop thorugh all configured events, 4. Request event data from GA4 API, 5. Export each event to CSV file
    cfg = load_config()                                                    
    client = get_client(cfg["ga4"]["key_file"])
    property_id = cfg["ga4"]["property_id"] 
    start_date = cfg["export"]["start_date"]
    end_date = cfg["export"]["end_date"] 
    output_folder = os.path.join(BASE_DIR, cfg["export"]["output_folder"])

    events = cfg["export"]["events"]

    for event_name in events: # loop through all configured events, fetch data and export to CSV
        print(f"Fetching: {event_name}")
        report = fetch_event_report(client, property_id, event_name, start_date, end_date)
        save_report_to_csv(report, event_name, output_folder)


if __name__ == "__main__": # Execute pipeline when script is run directly
    main()
