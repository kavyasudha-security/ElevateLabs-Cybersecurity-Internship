# Task 14 – Linux Server Hardening & Secure Configuration

## Overview
This task focuses on hardening a Linux system by applying secure configuration and best-practice controls. The objective is to reduce the attack surface, enforce least privilege, secure remote access, and ensure proper monitoring of system activity.

All activities were performed ethically in a controlled environment.

---

## Tools & Environment
- Linux OS (Kali Linux)
- systemctl
- ss
- apt package manager
- UFW (Uncomplicated Firewall)
- journalctl
- OpenSSH

---

## Objectives
- Review default Linux users, services, and open ports
- Enforce least privilege and review sudo access
- Harden SSH and disable root login
- Apply system updates and security patches
- Configure a firewall with a default-deny policy
- Reduce attack surface by reviewing running services
- Secure sensitive system files with strict permissions
- Monitor authentication and system activity logs

---

## Methodology
A structured hardening approach was followed:
1. Reviewed existing users, groups, services, and listening ports.
2. Verified sudo privileges to enforce the principle of least privilege.
3. Hardened SSH by disabling root login and validating secure service operation.
4. Updated system packages to apply security patches.
5. Configured firewall rules to allow only required network traffic.
6. Reviewed running services to ensure no unnecessary services were active.
7. Verified restricted permissions on sensitive system files.
8. Reviewed system and authentication logs for monitoring and auditing.

---

## Key Hardening Measures Implemented
- Principle of least privilege enforced through sudo access review
- SSH root login disabled to prevent direct administrative access
- SSH service securely enabled, restarted, and validated
- Firewall configured with default deny rules for inbound traffic
- System packages updated to mitigate known vulnerabilities
- Sensitive files protected using restricted file permissions
- Authentication and system activity monitored using logs

---

## Outcome
The Linux system was successfully hardened against common misconfigurations and attack vectors. Only essential services are active, sensitive files are protected, network access is restricted, and logging mechanisms are in place for monitoring and incident detection.

---

## Conclusion
This task demonstrates practical understanding of Linux server hardening aligned with industry best practices. The applied controls enhance system security, accountability, and resilience in real-world environments.

---

## Author
Cybersecurity Intern  
Elevate Labs Internship Program
