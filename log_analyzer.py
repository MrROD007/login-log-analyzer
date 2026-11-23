import csv
from pathlib import Path


# Settings: change the threshold to adjust when alerts are generated.
ALERT_THRESHOLD = 5
log_file = Path(__file__).resolve().parent / "sample_log.csv"

# Track totals and failed attempts for each IP address.
total_events = 0
successful_logins = 0
failed_logins = 0
failed_by_ip = {}

print("Login Log Analyzer")
print("==================")
print("Failed login attempts:\n")

with log_file.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for event in reader:
        total_events += 1

        if event["status"] == "SUCCESS":
            successful_logins += 1

        elif event["status"] == "FAILED":
            failed_logins += 1
            ip_address = event["ip_address"]

            # Start at zero for a new IP, then add one failure.
            failed_by_ip[ip_address] = (
                failed_by_ip.get(ip_address, 0) + 1
            )

            print(
                f"Time: {event['timestamp']} | "
                f"User: {event['username']} | "
                f"IP: {ip_address}"
            )

print("\nSummary")
print("-------")
print(f"Total login events: {total_events}")
print(f"Successful logins: {successful_logins}")
print(f"Failed logins: {failed_logins}")

print("\nFailed attempts by IP address")
print("----------------------------")

for ip_address, count in sorted(failed_by_ip.items()):
    print(f"{ip_address}: {count}")

print(f"\nAlerts: {ALERT_THRESHOLD} or more failures per IP")
print("----------------------------------------")

alerts_found = False

for ip_address, count in sorted(failed_by_ip.items()):
    if count >= ALERT_THRESHOLD:
        alerts_found = True
        print(
            f"ALERT: {ip_address} had {count} failed login attempts."
        )

if not alerts_found:
    print("No IP addresses reached the alert threshold.")

print("\nAlerts indicate activity for review, not confirmed attacks.")
print("Failures are counted across the entire file, not a time window.")

# Build a report containing the summary and flagged IP addresses.
report_file = Path(__file__).resolve().parent / "alert_report.txt"

report_lines = [
    "Login Security Alert Report",
    "===========================",
    f"Source file: {log_file.name}",
    f"Alert threshold: {ALERT_THRESHOLD} failures per IP",
    "",
    "Summary",
    "-------",
    f"Total login events: {total_events}",
    f"Successful logins: {successful_logins}",
    f"Failed logins: {failed_logins}",
    "",
    "Failed attempts by IP address",
    "----------------------------",
]

for ip_address, count in sorted(failed_by_ip.items()):
    report_lines.append(f"{ip_address}: {count}")

report_lines.extend([
    "",
    "Alerts",
    "------",
])

for ip_address, count in sorted(failed_by_ip.items()):
    if count >= ALERT_THRESHOLD:
        report_lines.append(
            f"ALERT: {ip_address} had {count} failed login attempts."
        )

if not alerts_found:
    report_lines.append("No IP addresses reached the alert threshold.")

report_lines.extend([
    "",
    "Alerts indicate activity for review, not confirmed attacks.",
    "Failures are counted across the entire file, not a time window.",
])

report_file.write_text(
    "\n".join(report_lines) + "\n",
    encoding="utf-8",
)

print(f"\nReport saved to: {report_file}")