# 🔐 Task 15 – Vulnerability Assessment & Risk Prioritization

## 📌 Overview
This task focuses on performing a vulnerability assessment using Nessus Essentials, identifying security weaknesses, classifying vulnerabilities using CVSS scoring, and prioritizing remediation actions based on risk level.

The assessment was conducted in a controlled lab environment to ensure safe and ethical testing.

---

## 🎯 Objective
- Perform a vulnerability scan using Nessus Essentials
- Identify detected vulnerabilities
- Analyze findings using CVSS scoring
- Map findings to Plugin IDs / CVE (where applicable)
- Classify vulnerabilities based on severity
- Create a structured Risk Priority List
- Recommend remediation actions

---

## 🛠 Tool Used
- Scanner: Nessus Essentials (Free Version)
- Scan Policy: Basic Network Scan
- Target: 127.0.0.1 (Localhost)
- Scan Mode: On-demand
- Scan Type: Non-authenticated

---

## 📍 Scope Definition
The scope of this vulnerability assessment was limited to:
- Localhost system (127.0.0.1)
- Controlled environment
- No external or third-party systems

This ensured compliance with ethical cybersecurity standards.

---

## ⚙️ Methodology
The vulnerability assessment followed the standard VA lifecycle:

1. Define Scope  
2. Configure Scanner  
3. Execute Scan  
4. Review Findings  
5. Map to CVSS & Plugin IDs  
6. Classify Risk  
7. Prioritize Vulnerabilities  
8. Recommend Remediation  

---

## 🔎 Scan Execution
The scan was initiated from the Nessus dashboard using the Basic Network Scan policy. During execution, Nessus performed:

- Host discovery  
- Port scanning  
- Service detection  
- Vulnerability plugin checks  
- CVSS severity assignment  

The scan completed successfully and generated detailed vulnerability results.

---

## 📊 Vulnerability Summary
- Total Vulnerabilities Identified: 24  
- Critical: 0  
- High: 0  
- Medium: Present  
- Low: Minimal  
- Informational: Multiple  

The highest severity identified was Medium, indicating moderate risk.

---

## ⚠ Key Vulnerability Identified

### SMB Signing Not Required
- Plugin ID: 57608  
- Severity: Medium  
- CVSS Score: 5.3  
- Port: 445/tcp  

### Risk Description
The SMB service does not require digital message signing. This may allow man-in-the-middle (MITM) attacks within internal network environments.

### Recommended Remediation
Enable SMB message signing in Windows Group Policy:

Microsoft network server: Digitally sign communications (always)

---

## 📈 Risk Prioritization

| Priority | Vulnerability | Severity | Recommended Action |
|----------|--------------|----------|-------------------|
| 1 | SMB Signing Not Required | Medium | Enable SMB signing |
| 2 | SSL/TLS Configuration Issues | Medium | Disable weak protocols |
| 3 | Informational Findings | Informational | Monitor and document |

Risk prioritization ensures that moderate-impact vulnerabilities are addressed before lower-severity issues.

---

## 🧠 Key Concepts Applied
- Vulnerability Assessment methodology  
- CVSS (Common Vulnerability Scoring System)  
- Plugin-based detection analysis  
- Risk classification matrix  
- Risk-based remediation planning  

---

## ⚠ Limitations
- Non-authenticated scan
- Limited to localhost environment
- Nessus Essentials free version does not support full PDF export
- Screenshots included as supporting evidence instead

---

## 🏁 Conclusion
The vulnerability assessment identified moderate configuration-based vulnerabilities on the local system. While no critical or high-risk findings were detected, remediation of medium-level vulnerabilities is recommended to enhance system security posture.

Regular vulnerability scanning and proactive remediation are essential components of effective cybersecurity management.
