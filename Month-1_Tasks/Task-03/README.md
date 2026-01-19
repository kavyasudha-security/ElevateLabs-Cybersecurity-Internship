# Task 3 – Networking Basics for Cybersecurity

## Internship: Cybersecurity Internship  
## Task Title: Networking Basics for Cybersecurity  
## Tools Used: Wireshark  
## Operating System: Kali Linux (VirtualBox)

---

## 📌 Objective
The objective of this task is to understand basic networking concepts by capturing and analyzing live network traffic using Wireshark.  
This task focuses on observing how common network protocols operate and how they are relevant from a cybersecurity perspective.

---

## 🛠 Environment & Tools
- **Kali Linux** – Virtual machine used for network analysis  
- **Wireshark** – Packet capture and network traffic analysis tool  
- **VirtualBox** – Virtualization platform  

---

## 📂 Repository Structure
ask-03/
│
├── Screenshots/
│ ├── icmp_ping.png
│ ├── dns_query.png
│ ├── http_traffic.png
│ ├── https_tls.png
│ └── tcp_handshake.png
│
├── task3_network_capture.pcapng
└── README.md
---

## 🧪 Practical Work Performed

### 1️⃣ ICMP Analysis
- Used `ping google.com` to generate ICMP traffic.
- Observed Echo Request and Echo Reply packets in Wireshark.

**Security Insight:**  
ICMP is useful for connectivity checks but can be abused for reconnaissance and flooding attacks.

---

### 2️⃣ DNS Analysis
- Used `nslookup google.com` to generate DNS queries.
- Observed DNS query and response packets using Wireshark.

**Security Insight:**  
DNS traffic reveals domain resolution and can be monitored to detect malicious or suspicious domains.

---

### 3️⃣ HTTP Traffic Analysis
- Accessed `http://neverssl.com`.
- Observed plaintext HTTP requests and headers.

**Security Insight:**  
HTTP traffic is unencrypted and vulnerable to interception and data exposure.

---

### 4️⃣ HTTPS / TLS Traffic Analysis
- Accessed `https://www.google.com`.
- Observed encrypted TLS traffic in Wireshark.

**Security Insight:**  
HTTPS protects data confidentiality by encrypting communication using TLS.

---

### 5️⃣ TCP Three-Way Handshake
- Observed SYN, SYN-ACK, and ACK packets using Wireshark filters.

**Security Insight:**  
The TCP handshake ensures reliable communication and helps detect abnormal or suspicious connection behavior.

---

## 📄 Packet Capture File
The captured network traffic is saved as:task3_network_capture.pcapng

📌 **Note:**  
If the packet capture file does not render in GitHub preview, please download and open it locally using Wireshark.

---

## 🎯 Learning Outcome
- Understanding of basic networking and protocol behavior  
- Hands-on experience with Wireshark  
- Ability to analyze encrypted vs unencrypted traffic  
- Practical understanding of network-based security risks  

---

## ✅ Task Status
✔ Completed  
✔ Screenshots included  
✔ Packet capture file included  

---

## 👤 Submitted By
**Name:** Kavya Sudha  
**Role:** Cybersecurity Intern
