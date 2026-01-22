# Task 05 – Malware Types and Behavior Analysis

## Overview
This task focuses on understanding different types of malware and analyzing their behavior using a safe and controlled approach. The objective is to study malware classification, detection methods, behavioral indicators, and prevention techniques through both theoretical concepts and practical analysis.

A real-world ransomware sample (WannaCry) was analyzed using VirusTotal to observe detection reports and malware behavior without executing any malicious files.

---

## Objectives
- Understand what malware is and why malware analysis is important
- Study common types of malware and their characteristics
- Analyze malware detection reports using VirusTotal
- Observe malware behavior indicators and lifecycle stages
- Understand how malware spreads across systems
- Learn basic prevention and mitigation techniques

---

## Tools and Platforms Used
- **VirusTotal** (hash-based malware analysis)
- **Web browser** for report analysis

---

## Practical Analysis Summary
- A known WannaCry ransomware hash was analyzed using VirusTotal
- Detection results from multiple antivirus engines were observed
- Malware classification, activity summary, and behavior indicators were studied
- Network communication, MITRE ATT&CK techniques, and dropped artifacts were reviewed
- Analysis was performed safely using hash-based lookup without downloading malware

---

## Folder Structure
Task-05/
│
├── Screenshots/
│ ├── VT_WannaCry_Detection.png
│ ├── VT_WannaCry_FileDetails.png
│ ├── VT_WannaCry_ActivitySummary.png
│ ├── VT_WannaCry_MitreAttack.png
│ ├── VT_WannaCry_Network.png
│ └── VT_WannaCry_DroppedFiles.png
│
├── Malware Types and Behavior Analysis.pdf
└── README.md

---

## Key Learnings
- Malware behaves differently based on its type and objective
- Behavior-based analysis is critical for identifying modern malware
- Ransomware like WannaCry combines encryption and network-based spreading
- Hash-based malware analysis allows safe and effective investigation
- Prevention strategies are essential to reduce malware impact

---

## Note
This analysis was conducted using publicly available malware hash information. No malware files were downloaded or executed during this task.

---

## Conclusion
This task provided practical insight into malware behavior and detection techniques. By combining theoretical understanding with VirusTotal analysis, a clear picture of how malware operates and how it can be mitigated was achieved.
