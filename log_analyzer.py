import csv
from pathlib import Path


# Find the sample log in the same folder as this script.
log_file = Path(__file__).resolve().parent / "sample_log.csv"

print("Login Log Analyzer")
print("==================")
print("Failed login attempts:\n")

# Open the CSV file and read each event using its column names.
with log_file.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for event in reader:
        if event["status"] == "FAILED":
            print(
                f"Time: {event['timestamp']} | "
                f"User: {event['username']} | "
                f"IP: {event['ip_address']}"
            )

print("\nLog review complete.")