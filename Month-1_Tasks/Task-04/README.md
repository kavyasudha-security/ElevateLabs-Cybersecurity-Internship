# Task 04 – Password Security and Authentication Analysis

## Overview
This task focuses on understanding how passwords are securely stored, analyzed, and protected in real-world systems. The objective is to study password hashing techniques, analyze why weak passwords fail, and understand the importance of strong authentication mechanisms through both theory and practical experimentation.

The task includes hands-on password hash generation and cracking using industry-standard tools, followed by an analysis of secure password practices and multi-factor authentication.

---

## Objectives
- Understand how passwords are stored using hashing instead of encryption
- Identify different hashing algorithms such as MD5, SHA-256, and bcrypt
- Generate password hashes and analyze their behavior
- Perform dictionary-based password cracking on weak hashes
- Compare fast and slow hashing algorithms
- Study the importance of Multi-Factor Authentication (MFA)
- Provide recommendations for strong authentication practices

---

## Tools Used
- **Kali Linux**
- **John the Ripper**
- **Hashcat**
- **rockyou.txt wordlist**

---

## Practical Summary
- Weak passwords were hashed using MD5, SHA-256, and bcrypt
- Dictionary attacks were performed using John the Ripper and Hashcat
- MD5 and SHA-256 hashes were cracked quickly when weak passwords were used
- bcrypt hashes showed stronger resistance due to salting and higher computational cost
- Results highlighted the importance of strong passwords and secure hashing algorithms

---

## Folder Structure
Task-04/
│
├── Screenshots/
│   ├── JTR_*.png
│   ├── HC_*.png
│   └── BC_*.png
│
├── wordlists/
│   └── sample_wordlist.txt
│
├── Password Security and Authentication Analysis.pdf
└── README.md


---

## Key Learnings
- Hashing is preferred over encryption for password storage
- Fast hashing algorithms are vulnerable to password cracking
- bcrypt is designed specifically for password security
- Weak passwords remain a major security risk
- Multi-Factor Authentication adds an essential layer of protection

---

## Note
If the PDF file does not render correctly in the GitHub preview, please download and open it locally for proper viewing.

---

## Conclusion
This task provided practical insight into password security mechanisms and reinforced the importance of using strong hashing algorithms along with secure authentication practices to protect systems against password-based attacks.
