# Linux Hardening Audit Tool v1.0

## Overview

Linux Hardening Audit Tool v1.0 is a Python-based command-line security auditing tool developed to evaluate the security posture of a Linux system. 

The tool performs multiple system-level hardening checks and generates structured audit reports along with an overall compliance score.

---

## Features Implemented

- Firewall Status Check (UFW)
- SSH Root Login Configuration Check
- Password Aging Policy Verification
- UID 0 Account Validation
- SUID Files Detection
- World-Writable Files Detection
- Listening Services and Ports Detection
- Compliance Score Calculation
- Risk Classification (SECURE / MODERATE RISK / HIGH RISK)
- Color-coded CLI output
- Report generation in TXT format
- Report generation in JSON format

---

## Project Structure

Week2_Linux_Hardening_Audit_Tool/
    main.py
    audit_checks.py
    report_generator.py
    README.md

---

## Requirements

- Linux System (Tested on Kali Linux)
- Python 3.x
- sudo privileges

---

## How to Run

sudo python3 main.py

---

## Sample Output

=== Linux Hardening Audit Tool v1.0 ===

[PASS] Firewall - UFW firewall is active.
[PASS] SSH Root Login - Root login disabled.
[PASS] Password Policy - Password aging policy configured.
[PASS] UID 0 Accounts - Only root has UID 0.
[INFO] SUID Files - Number of SUID files found: 34
[INFO] World Writable Files - World-writable files found: 0
[INFO] Listening Services - Number of listening ports: 0

Overall Compliance Score: 100.00%
System Status: SECURE

Reports saved as:
- audit_report.txt
- audit_report.json

---

## Version

v1.0 – Stable Release

---

## Learning Outcomes

- Linux system hardening concepts
- Security audit automation using Python
- Modular programming structure
- Compliance scoring logic
- CLI tool development
- Report generation techniques