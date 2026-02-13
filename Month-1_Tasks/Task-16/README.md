# 🛡 Task 16 – Incident Response & Security Breach Simulation

## 📌 Overview
This task demonstrates a structured Incident Response (IR) simulation using Windows Event Viewer. The objective was to detect, analyze, classify, and document authentication-related security events in a controlled lab environment.

The simulation focused on failed login attempts recorded in Windows Security Logs.

---

## 🎯 Objective
- Simulate failed login attempts
- Detect suspicious authentication activity
- Analyze Event ID 4625 (Failed Logon)
- Correlate with Event ID 4624 (Successful Logon)
- Perform root cause analysis
- Classify incident severity
- Document containment actions
- Create an incident timeline

---

## 🖥 Environment Details

- Operating System: Windows 11
- Log Monitoring Tool: Windows Event Viewer
- Log Location: Windows Logs → Security
- Event ID Analyzed:
  - 4625 – Failed Logon Attempt

---

## 🔍 Incident Simulation

The incident was simulated by generating failed authentication attempts on the system.

Two failed logon events were recorded:

- 12-02-2026 at 13:50:10
- 13-02-2026 at 14:45:37

Both events were logged under:

- Log Level: Audit Failure
- Task Category: Logon

---

## 📊 Log Analysis Findings

- Total Failed Logon Events: 2
- Event ID: 4625
- Status Code: 0xC000006D (Authentication Failure)
- Sub Status Code: 0xC0000072
- No correlated successful suspicious logins (Event ID 4624)
- No rapid or repeated login attempts observed

The limited frequency and absence of repeated attempts indicated no brute-force activity.

---

## ⚠ Incident Classification

- Incident Type: Failed Authentication Attempts
- Frequency: Two isolated occurrences
- Pattern: Non-persistent
- Severity Level: Low
- System Impact: None

The incident was classified as Low Severity since no successful unauthorized access occurred.

---

## 🧠 Root Cause Analysis

Root cause analysis determined that the failed login attempts were most likely caused by incorrect credential entry.

There was no evidence of:

- Brute-force attack
- Credential stuffing
- Account compromise
- Privilege escalation
- Malware activity

The activity was consistent with normal authentication error.

---

## 🛡 Containment & Response

Although the severity was low, verification steps were performed:

- Reviewed additional authentication logs
- Checked for Event ID 4624
- Verified system integrity
- Confirmed no account lockout

No containment or eradication measures were required.

Final Status:

Incident Closed – No Breach Confirmed

---

## 📅 Incident Timeline

| Date       | Time     | Event ID | Description            | Action Taken |
|------------|----------|----------|------------------------|--------------|
| 12-02-2026 | 13:50:10 | 4625     | Failed Logon Attempt   | Log Reviewed |
| 13-02-2026 | 14:45:37 | 4625     | Failed Logon Attempt   | Verified & Analyzed |

---

## 📈 Preventive Recommendations

- Enable account lockout policy
- Implement Multi-Factor Authentication (MFA)
- Configure authentication failure alerts
- Regularly monitor Event ID 4625 and 4624
- Enforce strong password policies

---

## 📚 Skills Demonstrated

- Security log analysis
- Event ID filtering and correlation
- Incident classification
- Root cause analysis
- Risk-based assessment
- Incident documentation
- Timeline reporting

---

## 🏁 Conclusion

The incident response simulation successfully demonstrated structured detection and analysis of authentication events using Windows Event Viewer.

The system remained secure, and no compromise was detected.

This task reflects practical understanding of real-world incident handling procedures.
