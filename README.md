# Automated Login Log Analyzer and Security Alert Generator

## Project Overview
This is my individual security automation class project. I built a
Python program that reads a saved CSV file of fictional login events,
counts failed attempts by IP address, and generates alerts for IP
addresses that meet or exceed a configurable threshold. The program
displays the results in Terminal and saves an alert report.


## Implemented Features

- Reads fictional login events from sample_log.csv.
- Displays failed login events with timestamps, usernames, and IP addresses.
- Counts total events, successful logins, and failed logins.
- Groups failed login attempts by IP address.
- Flags IP addresses that meet or exceed a configurable threshold.
- Displays a summary and alerts in Terminal.
- Saves the summary and alerts to alert_report.txt.

## How to Run

1. Download or clone this repository.
2. Open Terminal in the project folder.
3. Run:

   python3 log_analyzer.py

4. Review the Terminal output and open alert_report.txt.

Python 3 is required. No additional Python packages are required.

## Configuration

The default alert threshold is five failed login attempts per IP address.

To change it, edit this setting near the top of log_analyzer.py:

ALERT_THRESHOLD = 5

Save the script and run it again to apply the new threshold.

Each run replaces alert_report.txt with the latest results.

## Testing Results

The sample file contains 10 fictional login events:
3 successful logins and 7 failed logins.

Failed attempts by IP:
- 192.0.2.20: 5 failures
- 192.0.2.30: 2 failures

I manually tested these thresholds:

| Threshold | Expected Alerts | Result |
|-----------|-----------------|--------|
| 6 | No alerts | Passed |
| 2 | Both IP addresses | Passed |
| 5 | Only 192.0.2.20 | Passed |

The threshold was restored to 5 after testing.

## Scope and Limitations

- Uses a saved CSV file, not live monitoring.
- Counts failures across the entire file, not within a time window.
- Expects the column names timestamp, username, ip_address, and status.
- Expects status values of SUCCESS or FAILED.
- Does not send notifications or block IP addresses.
- An alert identifies activity for review; it does not confirm an attack.
- Testing so far used the supplied fictional sample data.

## AI Assistance
I used Perplexity to help plan the project, explain Python concepts,
and provide step-by-step development guidance. It also helped me
troubleshoot GitHub authentication and a filename mismatch.

I reviewed and ran the suggested code, checked the output against
the fictional sample data, and manually tested three alert thresholds.
AI also helped organize the README and testing documentation.