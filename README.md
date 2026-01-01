# cybersecurity-fundamentals-projects

🛡️ Cybersecurity Fundamentals – Hands-On Project Suite

This repository contains a collection of hands-on cybersecurity projects developed to gain practical exposure to network security, web application security, Linux system hardening, password security, and network traffic analysis.

The work focuses on understanding real-world security issues, identifying common vulnerabilities, and applying basic defensive security practices using industry-standard tools in controlled lab environments.

📂 Repository Structure
cybersecurity-fundamentals-projects/
│
├── README.md
│
├── network-recon/
│   ├── nmap_commands.txt
│   ├── scan_results.txt
│   ├── findings_report.md
│   └── logs/
│       ├── nmap_scan.log
│       └── nmap_service_detection.log
│
├── web-vulnerability-testing/
│   ├── burp_requests.txt
│   ├── vulnerability_report.md
│   └── logs/
│       ├── burp_proxy.log
│       └── burp_repeater.log
│
├── password-manager/
│   ├── password_manager.py
│   ├── README.md
│   └── logs/
│       └── app.log
│
├── traffic-analysis/
│   ├── wireshark_filters.txt
│   ├── analysis_report.md
│   └── logs/
│       ├── packet_capture.log
│       └── dns_capture.log
│
├── linux-security/
│   ├── hardening_commands.sh
│   ├── security_notes.md
│   └── logs/
│       ├── auth.log
│       └── ufw.log
│
└── docs/
    └── final_report.md

1️⃣ Network Reconnaissance & Port Scanning
🎯 Objective

To identify live hosts, open ports, and running services and understand their basic security implications.

🛠 Tools

Nmap

Kali Linux

📌 Work Performed

Host discovery on local network

TCP port scanning

Service and version detection

Documentation of exposed services

📄 Evidence

Commands: nmap_commands.txt

Scan output: scan_results.txt

Logs: logs/nmap_scan.log

Findings report: findings_report.md

🔍 Key Learnings

Open ports increase attack surface

Service version disclosure may reveal vulnerabilities

Unused services should be disabled

2️⃣ Web Application Vulnerability Testing (OWASP Top 10)
🎯 Objective

To identify common web vulnerabilities using intentionally vulnerable applications.

🛠 Tools

Burp Suite

DVWA / OWASP Juice Shop

📌 Vulnerabilities Tested

SQL Injection (SQLi)

Cross-Site Scripting (XSS)

Input validation flaws

📄 Evidence

Intercepted requests: burp_requests.txt

Logs: logs/burp_proxy.log, logs/burp_repeater.log

Vulnerability analysis: vulnerability_report.md

🔍 Key Learnings

Improper input validation leads to serious attacks

Authentication mechanisms can be bypassed

Secure coding practices are essential

3️⃣ Password Management System
🎯 Objective

To understand secure password storage concepts and basic access control.

🛠 Technology

Python

📌 Features Implemented

Password hashing (SHA-256)

Simple authentication logic

No plaintext password storage

📄 Evidence

Code: password_manager.py

Logs: logs/app.log

Explanation: password-manager/README.md

🔍 Key Learnings

Hashing protects stored credentials

Plaintext password storage is insecure

Authentication logic must be carefully implemented

4️⃣ Network Traffic Analysis
🎯 Objective

To analyze network packets and understand protocol behavior and insecure communication.

🛠 Tool

Wireshark

📌 Work Performed

Live traffic capture

Protocol filtering (HTTP, DNS, TCP)

Packet inspection

📄 Evidence

Filters used: wireshark_filters.txt

Logs: logs/packet_capture.log, logs/dns_capture.log

Analysis report: analysis_report.md

🔍 Key Learnings

HTTP traffic transmits data in plaintext

DNS traffic reveals queried domains

Encryption is critical for secure communication

5️⃣ Linux System Security Configuration
🎯 Objective

To implement basic Linux system hardening techniques.

🛠 Tools & Commands

Linux permissions

UFW firewall

System service auditing

📌 Tasks Performed

User permission management

Firewall rule configuration

Identification of unnecessary services

📄 Evidence

Commands: hardening_commands.sh

Logs: logs/auth.log, logs/ufw.log

Notes: security_notes.md

🔍 Key Learnings

Proper permissions prevent unauthorized access

Firewalls restrict unwanted network traffic

Service auditing reduces system exposure

🧠 Skills & Concepts Gained

Network reconnaissance and scanning

Web application security testing

OWASP Top 10 fundamentals

Password security & hashing

Network traffic analysis

Linux security hardening

⚠️ Disclaimer

All activities in this repository were performed in controlled lab environments or intentionally vulnerable applications for educational purposes only.

No unauthorized systems, networks, or applications were tested.

Some logs are simulated to reflect realistic system behavior for learning and documentation purposes.

✅ Conclusion

This project demonstrates foundational cybersecurity skills with practical exposure to both offensive and defensive security concepts.
It is suitable for internship evaluation, academic submission, and beginner-level cybersecurity roles.
