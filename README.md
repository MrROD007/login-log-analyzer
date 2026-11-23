# Automated Login Log Analyzer and Security Alert Generator

## Project Overview
This is my individual security automation class project. I am building
a Python program that reads a saved sample login log and identifies
failed login attempts.

## Planned Features
- Read login events from a sample log file.
- Identify failed login attempts.
- Count failed attempts by IP address.
- Flag IP addresses that reach a configurable failure threshold.
- Display a summary and save an alert report.

## Scope
This project uses fictional sample data rather than live system logs.
The initial alert threshold will be five failed attempts per IP address
across the entire file. An alert indicates activity worth reviewing,
not a confirmed attack.

## Current Progress
- Created the GitHub repository and local project folder.
- Added fictional sample login data.
- Created a Python script that reads the sample CSV file.
- Confirmed that the script displays the seven expected failed login events.

## Next Steps
- Count failed login attempts by IP address.
- Add a configurable alert threshold.
- Save an alert report.
- Test additional sample files and document the results.

## AI Assistance
I used Perplexity to help plan the project and provide step-by-step
guidance. I will review and test suggested code so I understand
how the program works.