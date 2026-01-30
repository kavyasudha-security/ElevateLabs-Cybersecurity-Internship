# Task 10 – Firewall Configuration and Testing Using UFW

## 📌 Overview
This task focuses on configuring and testing a host-based firewall to control network traffic and enhance system security. The objective is to understand firewall concepts, configure allow and deny rules, test connectivity, enable logging, and analyze the security impact of firewall enforcement.

All activities were performed in a controlled lab environment using Kali Linux.

---

## 🛠 Tools & Environment
- **Operating System:** Kali Linux
- **Firewall Tool:** UFW (Uncomplicated Firewall)
- **Testing Tool:** Nmap
- **Target System:** Localhost (127.0.0.1)
- **Active Services:** SSH, HTTP (Apache), MySQL (MariaDB)

---

## 🎯 Objectives
- Install and configure a firewall using UFW
- Define default inbound and outbound firewall policies
- Allow essential services and block unauthorized access
- Test firewall rules using network scanning
- Enable logging and demonstrate IP-based blocking
- Analyze the impact of firewall rules on system security

---

## 🧪 Methodology

### 1. Firewall Installation and Setup
UFW was installed on Kali Linux and verified for proper functionality.

### 2. Enabling Firewall
The firewall was enabled to begin enforcing network traffic rules.

### 3. Default Policy Configuration
- Incoming traffic was denied by default
- Outgoing traffic was allowed

### 4. Firewall Rule Configuration
Firewall rules were configured to:
- Allow SSH (Port 22)
- Allow HTTP (Port 80)
- Allow MySQL (Port 3306)
All other incoming traffic was restricted.

### 5. Rule Verification
Firewall rules were verified using verbose status output to ensure correct enforcement.

### 6. Connectivity Testing
Nmap scans were performed after firewall configuration to confirm that only allowed services were accessible.

### 7. Logging and Monitoring
Firewall logging was enabled to observe allowed and blocked traffic.

### 8. Blocking Malicious Traffic
A sample IP address was blocked to demonstrate firewall-based access control.

---

## 🔍 Observations
- Firewall rules successfully restricted unauthorized access
- Only explicitly allowed ports remained accessible
- Network scans reflected filtered and blocked ports after firewall enforcement
- Logging provided visibility into firewall activity

---

## ⚠ Impact Analysis
Firewall configuration significantly reduces the system’s attack surface by limiting exposed services and enforcing access control. While firewalls provide strong network-level protection, they must be used alongside other security measures to protect against application-level and social engineering attacks.

---

## 🛡 Best Practices
- Deny incoming traffic by default
- Allow only required services
- Regularly review firewall rules
- Enable logging and monitoring
- Combine firewall usage with system updates and secure configurations

---

## ✅ Conclusion
This task demonstrated effective firewall configuration and testing using UFW. By applying security rules, verifying configurations, and testing connectivity, the task highlights the importance of firewalls in strengthening system security and controlling network access.

---

## 👤 Author
**Intern – Cybersecurity**  
**Elevate Labs Internship Program**
