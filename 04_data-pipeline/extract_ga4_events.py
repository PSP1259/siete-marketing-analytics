import os
import yaml
import pandas as pd
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest,
    DateRange,
    Metric,
    Dimension,
    Filter,
    FilterExpression,)
from google.oauth2 import service_account

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_config():
    if os.path.exists(os.path.join(BASE_DIR, "config.yaml")):
        config_path = os.path.join(BASE_DIR, "config.yaml")
    else:
        config_path = os.path.join(BASE_DIR, "config_example.yaml")

    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_client(key_file):
    credentials = service_account.Credentials.from_service_account_file(key_file)
    return BetaAnalyticsDataClient(credentials=credentials)


def fetch_event_data(client, property_id, event_name, start_date, end_date):
    request = RunReportRequest(
        property=f"properties/{property_id}",
        metrics=[
            Metric(name="eventCount"),
        ],
        dimensions=[
            Dimension(name="date"),
        ],
        date_ranges=[
            DateRange(start_date=start_date, end_date=end_date),
        ],
    )
    return client.run_report(request)



def save_report_to_csv(report, event_name, output_folder):
    rows = []
    for row in report.rows:
        rows.append({
            "date": row.dimension_values[0].value,
            "event_name": event_name,
            "event_count": int(row.metric_values[0].value),
        })

    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, f"{event_name}.csv")
    df = pd.DataFrame(rows)
    df.to_csv(output_path, index=False)
    print(f"Exported: {output_path}")




def main():
    cfg = load_config()

    client = get_client(cfg["ga4"]["key_file"])
    property_id = cfg["ga4"]["property_id"]
    start_date = cfg["export"]["start_date"]
    end_date = cfg["export"]["end_date"]
    output_folder = os.path.join(BASE_DIR, cfg["export"]["output_folder"])

    for event in cfg["export"]["events"]:
        print(f"Fetching: {event}")
        report = fetch_event_data(client, property_id, event, start_date, end_date)
        save_report_to_csv(report, event, output_folder)


if __name__ == "__main__":
    main()

