# Task 07 – Web Application Vulnerability Testing

## 📌 Overview
This project focuses on identifying and analyzing common web application vulnerabilities using **Burp Suite Community Edition** on a deliberately vulnerable application (**DVWA – Damn Vulnerable Web Application**).  
The objective is to understand how real-world web vulnerabilities occur, how attackers exploit them, and how such issues can be mitigated using secure coding practices.

---

## 🛠 Tools & Environment
- **Operating System:** Kali Linux
- **Vulnerable Application:** DVWA (Damn Vulnerable Web Application)
- **Web Server:** Apache
- **Database:** MariaDB (MySQL)
- **Testing Tool:** Burp Suite Community Edition
- **Browser:** Burp Suite embedded browser / Firefox (proxy configured)

---

## 🔐 Core Concepts Covered
- Web application architecture
- HTTP request and response structure
- Proxy-based traffic interception
- Input validation and insecure input handling
- OWASP Top 10 vulnerabilities overview

---

## 📚 OWASP Top 10 (2025) – Overview
The OWASP Top 10 represents the most critical security risks to web applications.  
This project primarily focuses on vulnerabilities related to **Injection** and **Cross-Site Scripting (XSS)** while understanding the broader OWASP framework.

### OWASP Top 10 (2025):
1. A01: Broken Access Control  
2. A02: Security Misconfiguration  
3. A03: Software Supply Chain Failures  
4. A04: Cryptographic Failures  
5. A05: Injection  
6. A06: Insecure Design  
7. A07: Authentication Failures  
8. A08: Software or Data Integrity Failures  
9. A09: Security Logging and Alerting Failures  
10. A10: Mishandling of Exceptional Conditions  

---

## 🧪 Practical Testing Performed

### 🔹 Burp Suite Interception
- Intercepted **GET** and **POST** HTTP requests
- Observed request headers, parameters, and cookies
- Forwarded and analyzed intercepted traffic
- Reviewed server responses using HTTP History

---

### 🔹 SQL Injection Testing
- Tested input fields with crafted SQL payloads
- Observed unauthorized database data retrieval
- Identified lack of input sanitization
- Classified vulnerability under **OWASP A05: Injection**

**Impact:**
- Unauthorized access to sensitive data
- Potential data leakage or manipulation

---

### 🔹 Cross-Site Scripting (XSS) Testing
- Injected JavaScript payloads into input fields
- Successfully executed scripts in the browser
- Observed alert pop-ups indicating reflected XSS
- Classified vulnerability under **OWASP Injection / XSS category**

**Impact:**
- Client-side code execution
- Session hijacking risks
- User data theft

---

## 🔍 Observations
- The application does not validate or sanitize user input
- Server responses differ significantly for malicious inputs
- Burp Suite effectively reveals hidden request details
- Vulnerabilities are easily exploitable when security controls are absent

---

## 🛡 Mitigation & Prevention Techniques
- Use **prepared statements** for database queries
- Implement **input validation and sanitization**
- Apply **output encoding** to prevent XSS
- Follow secure coding best practices
- Enforce least privilege access controls
- Regularly test applications using security tools

---

## 📄 Deliverables
- Vulnerability assessment report
- Screenshots of Burp Suite interception
- Documentation of SQL Injection and XSS attacks
- Mitigation strategies and security recommendations

---

## ✅ Conclusion
This task provided hands-on experience in web application security testing.  
By using Burp Suite and DVWA, real-world vulnerabilities such as SQL Injection and XSS were identified, analyzed, and documented.  
The exercise strengthened practical understanding of web security risks and reinforced the importance of secure development practices.

---

## 👤 Author
**Intern – Cybersecurity**  
Elevate Labs Internship Program
