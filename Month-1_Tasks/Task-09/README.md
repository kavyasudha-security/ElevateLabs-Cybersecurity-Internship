# Task 9 – Network Vulnerability Scanning Using Nmap

## 📌 Overview
This task focuses on performing **network vulnerability scanning** to identify open ports, running services, and potential security risks within a networked system. The objective is to understand how exposed services increase the attack surface and how such information can be used for security assessment.

All scanning activities were conducted in a **controlled local lab environment** using Kali Linux and Nmap.

---

## 🛠 Tools & Environment
- **Operating System:** Kali Linux
- **Target Host:** Localhost (127.0.0.1)
- **Scanning Tool:** Nmap
- **Active Services:**
  - Apache (HTTP)
  - OpenSSH (SSH)
  - MariaDB (MySQL)

---

## 🧪 Scanning Methodology

### 1. Service Initialization
Required services such as Apache and MariaDB were started to simulate an active system with exposed network services.

### 2. Basic Port Scanning
A basic Nmap scan was performed to identify open TCP ports on the local system.

### 3. Service and Version Detection
Service detection was carried out to determine the applications and versions running on the open ports.

### 4. Operating System Detection
Nmap OS fingerprinting was used to infer the underlying operating system based on TCP/IP characteristics.

---

## 🔍 Scan Findings
The network scan revealed the following open ports and services:

- **Port 22 (SSH):** Secure remote access service
- **Port 80 (HTTP):** Apache web server
- **Port 3306 (MySQL):** MariaDB database service

The operating system was identified as a **Linux-based system**, which is expected in a local virtualized environment.

---

## ⚠ Risk Interpretation
Open ports and exposed services increase the system’s attack surface. If misconfigured or outdated, these services may be exploited by attackers through techniques such as brute-force attacks, service misconfigurations, or known software vulnerabilities.

Regular network scanning helps in identifying such risks early and strengthens system security.

---

## 🛡 Mitigation & Recommendations
- Close unused ports and disable unnecessary services
- Restrict access to critical services using firewalls
- Keep operating systems and services updated
- Use strong authentication for SSH and database access
- Perform regular network vulnerability scans

---

## 📄 Deliverables
- Network scan results with documented evidence
- Identification of open ports and running services
- Risk interpretation and mitigation strategies
- Screenshot-based proof of scanning activities

---

## ✅ Conclusion
This task demonstrated the use of Nmap for network vulnerability scanning in a controlled environment. By identifying open ports, detecting services, and interpreting potential risks, the task emphasized the importance of proactive security assessment in maintaining a secure network infrastructure.

---

## 👤 Author
**Intern – Cybersecurity**  
**Elevate Labs Internship Program**
