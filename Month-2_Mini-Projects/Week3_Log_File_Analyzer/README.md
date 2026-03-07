# Week 3 Log File Analyzer for Intrusion Detection

## Overview
The Log File Analyzer for Intrusion Detection is a Python-based security monitoring tool designed to analyze authentication logs and detect suspicious login activities. The tool scans log files for failed login attempts and identifies potential brute-force attacks based on repeated login failures from the same IP address.

This project simulates a basic intrusion detection mechanism commonly used in Security Operations Centers (SOC) to monitor unauthorized access attempts.

## Features
- Parses system authentication logs.
- Detects failed login attempts.
- Identifies suspicious IP addresses.
- Detects possible brute-force attacks.
- Generates an automated security report.
- Assigns risk levels based on number of login attempts.

## Technologies Used
- Python
- Regular Expressions (regex)
- Collections Module (Counter)

## Project Structure
Week3_Log_File_Analyzer
│
├── main.py
├── log_parser.py
├── detector.py
├── report_generator.py
├── README.md
└── Week3_Log_File_Analyzer_Report.pdf

## How It Works

1. The log parser reads a log file containing authentication events.
2. Failed login attempts are extracted using pattern matching.
3. The detection module counts the number of attempts per IP address.
4. If the number of attempts exceeds a threshold, the IP is flagged as suspicious.
5. A detailed intrusion detection report is generated.

## Example Output

=== Intrusion Detection Report ===

Total Failed Login Attempts: 7

IP Attempt Counts:
192.168.1.15 -> 5 attempts
10.0.0.7 -> 2 attempts

Suspicious IPs (Possible Brute Force):
192.168.1.15 -> 5 attempts (HIGH RISK)

## Learning Outcomes

- Understanding of log analysis
- Basic intrusion detection concepts
- Pattern matching using regex
- Python scripting for cybersecurity automation
- Detecting brute-force login attacks

## Author
Cybersecurity Internship Project