# Task 12 – Log Monitoring & Analysis

## 📌 Overview
This task focuses on monitoring and analyzing system logs to detect authentication events, failed login attempts, anomalies, and correlated activities in a Linux environment. The objective is to understand how logs support security monitoring, incident detection, and forensic analysis.

All activities were performed in a controlled lab environment using Kali Linux with systemd-based logging.

---

## 🛠 Tools & Environment
- **Operating System:** Kali Linux
- **Logging Mechanism:** systemd-journald
- **Primary Commands:** journalctl, grep
- **Log Sources:** Authentication logs, system logs, SSH service logs

---

## 🎯 Objectives
- Understand different types of logs in Linux
- Analyze authentication-related log events
- Identify failed login attempts
- Detect anomalous behavior patterns
- Correlate related system and authentication events
- Learn SIEM concepts at a theoretical level
- Define security alert conditions
- Document findings from log analysis

---

## 🧪 Methodology

### 1. Log Types Identification
System log directories were explored to understand available log sources and their purposes.

### 2. Authentication Log Analysis
Authentication events were analyzed using `journalctl`, focusing on SSH activity and sudo usage.

### 3. Failed Login Detection
Authentication failures and unsuccessful access attempts were identified from system logs.

### 4. Anomaly Detection
Repeated authentication attempts, protocol errors, and unusual sudo activity were analyzed as anomalous patterns.

### 5. Event Correlation
SSH service lifecycle events were correlated with authentication attempts using timestamps to understand event relationships.

### 6. SIEM Basics (Conceptual)
Basic SIEM concepts were studied to understand centralized log collection, correlation, and alerting without deploying a SIEM tool.

---

## 🔐 SIEM Tools Overview
Security Information and Event Management (SIEM) tools are used to centralize logs, correlate events, and generate alerts. Common SIEM tools include:
- **Splunk** – Log aggregation, search, visualization, and alerting
- **IBM QRadar** – Real-time threat detection and correlation
- **Elastic Stack (ELK)** – Log ingestion, indexing, and visualization
- **ArcSight** – Enterprise-scale security monitoring

These tools automate log analysis and improve detection efficiency.

---

## 🚨 Alerting & Incident Awareness

### Sample Security Alert Conditions
- Alert when **multiple failed login attempts** occur within a short time window
- Alert on **repeated sudo privilege escalation attempts**
- Alert when **SSH service restarts unexpectedly**
- Alert on **authentication attempts from unknown users**

These alert conditions help reduce response time and improve incident handling.

---

## 📄 Findings
- Authentication and SSH activity were successfully monitored
- Failed login attempts and anomalies were identified
- Event correlation helped establish activity timelines
- No successful security breach was observed during analysis

---

## ⚠ Limitations
Manual log analysis is effective for learning and small systems but becomes impractical at scale due to high log volume. Automated tools and SIEM platforms are required for real-time analysis and alerting in enterprise environments.

---

## ✅ Conclusion
This task demonstrated the importance of log monitoring and analysis in cybersecurity. By examining authentication logs, detecting anomalies, correlating events, and defining alert conditions, the task highlights how logs support incident detection and security awareness.

---

## 👤 Author
**Intern – Cybersecurity**  
**Elevate Labs Internship Program**
