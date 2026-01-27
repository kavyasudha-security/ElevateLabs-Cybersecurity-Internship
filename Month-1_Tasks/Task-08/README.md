# Task 08 – SQL Injection Practical Exploitation

## 📌 Overview
This task focuses on the practical exploitation of **SQL Injection** vulnerabilities using an intentionally vulnerable web application. The objective of this task is to understand how SQL Injection vulnerabilities arise, how they can be exploited using automated tools, and the potential impact such vulnerabilities can have on web applications.

All testing was performed in a **controlled and ethical lab environment** using DVWA and SQLMap.

---

## 🛠 Tools & Environment
- **Operating System:** Kali Linux  
- **Vulnerable Application:** Damn Vulnerable Web Application (DVWA)  
- **Web Server:** Apache  
- **Database Server:** MariaDB (MySQL)  
- **Exploitation Tool:** SQLMap  

---

## 🔐 Vulnerability Tested
- **SQL Injection (SQLi)**  
  - GET-based SQL Injection  
  - Union-based SQL Injection  
  - Time-based Blind SQL Injection  

---

## 🧪 Testing Methodology

### 1. Lab Setup
- Apache and MariaDB services were started.
- DVWA was configured and accessed locally.
- Security level was set to **Low** to allow vulnerability testing.

### 2. Identification of Vulnerable Parameter
- The `id` parameter in the DVWA SQL Injection module was identified as injectable.
- Manual SQL Injection payloads confirmed improper input validation.

### 3. Automated Exploitation Using SQLMap
- SQLMap was used to verify the vulnerability.
- Backend DBMS was identified as **MySQL**.
- Injection techniques such as **Union-based** and **Time-based Blind SQL Injection** were detected.

### 4. Database and Table Enumeration
- Accessible databases were enumerated.
- The `dvwa` database was identified as the target.
- Sensitive tables such as `users` and `guestbook` were extracted.

### 5. User Data Extraction
- SQLMap successfully dumped user credentials from the `users` table.
- Password hashes were retrieved, and weak hashes were cracked using dictionary-based techniques.

---

## 🔍 Observations
- The application failed to validate and sanitize user input.
- Dynamic SQL queries were constructed using unsanitized parameters.
- SQL Injection allowed unauthorized access to backend databases.
- Sensitive authentication data was exposed through automated exploitation.

---

## ⚠ Impact Analysis
If exploited in a real-world application, SQL Injection vulnerabilities could lead to:
- Unauthorized access to sensitive data
- Credential compromise and account takeover
- Data manipulation or deletion
- Full backend database compromise
- Financial and reputational damage

---

## 🛡 Mitigation & Prevention Techniques
- Use prepared statements and parameterized queries
- Implement strict input validation and sanitization
- Follow the principle of least privilege for database accounts
- Avoid displaying detailed database error messages
- Conduct regular security testing and code reviews
- Store passwords using strong hashing algorithms with proper salting

---

## 📄 Deliverables
- Vulnerability assessment documentation
- Screenshot-based evidence of exploitation
- Database and user data extraction proof
- Impact analysis and mitigation recommendations

---

## ✅ Conclusion
This task demonstrated the complete SQL Injection exploitation lifecycle using SQLMap in a controlled lab environment. The successful extraction of databases, tables, and user credentials highlights the severity of SQL Injection vulnerabilities and emphasizes the importance of secure coding practices and proactive security testing.

---

## 👤 Author
**Intern – Cybersecurity**  
**Elevate Labs Internship Program**
