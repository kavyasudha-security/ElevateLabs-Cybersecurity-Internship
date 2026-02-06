# Task 13 – Secure API Testing & Authorization Validation

## 📌 Overview
This task focuses on understanding and testing API security concepts such as authentication, authorization, input validation, rate limiting, and secure error handling. The objective is to analyze how APIs enforce access control and handle invalid or unauthorized requests using a safe and ethical testing approach.

All testing was performed on publicly available test APIs using Postman, without exploiting or attacking real-world systems.

---

## 🛠 Tools & Environment
- **Tool Used:** Postman
- **Platform:** Windows (Host System)
- **APIs Tested:** Public test APIs (Postman Echo, ReqRes, JSONPlaceholder)
- **Testing Type:** Manual and ethical API security testing

---

## 🎯 Objectives
- Understand REST API fundamentals and HTTP methods
- Test API authentication with missing and invalid credentials
- Validate authorization and access control mechanisms
- Perform input validation testing
- Observe rate limiting and abuse prevention behavior
- Review HTTP response codes and error handling
- Map observations to OWASP API Security risks

---

## 🧪 Methodology
- API requests were manually created and sent using Postman
- Authentication was tested by providing valid, invalid, and missing credentials
- Authorization was tested by modifying resource identifiers (IDOR-style testing)
- Input validation was tested using malformed request payloads
- Rate limiting behavior was observed through repeated requests
- API responses and status codes were analyzed for security implications
- Testing scope was limited to public test APIs to maintain ethical standards

---

## 🔐 Key Tests Performed
- Authentication enforcement (401 / 403 responses)
- Authorization and resource access control
- Input validation and secure error handling
- Rate limiting observation
- HTTP response code analysis

---

## 🛡 OWASP API Security Risk Mapping
- **Broken Object Level Authorization (BOLA / IDOR)**
- **Broken Authentication**
- **Improper Input Validation**
- **Security Misconfiguration**

Observed behaviors were mapped conceptually to OWASP API Security risks without exploiting real vulnerabilities.

---

## 📄 Findings
- APIs correctly rejected unauthenticated and invalid requests
- Authorization checks behaved as expected for public APIs
- Malformed input was safely rejected
- No sensitive error information was disclosed
- No critical vulnerabilities were exploited during testing

---

## ⚠ Limitations
Rate limiting behavior was not explicitly enforced for unauthorized requests in the test APIs. In real-world production environments, APIs should implement strong rate-limiting and monitoring mechanisms to prevent abuse.

---

## ✅ Conclusion
This task provided practical exposure to API security testing using a structured and ethical approach. By analyzing authentication, authorization, input validation, and response behavior, the task reinforced the importance of secure API design and OWASP-aligned security practices.

---

## 👤 Author
**Intern – Cybersecurity**  
**Elevate Labs Internship Program**
