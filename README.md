# SentinelParser

A Python-based SIEM-style log parser designed to identify suspicious login activity and detect potential brute-force attacks.

## Features

- Parses authentication log files
- Counts failed login attempts
- Identifies unique attack sources
- Assigns severity levels
- Detects potential brute-force attacks
- Generates incident reports automatically

## Technologies Used

- Python 3
- Collections Module
- Git
- GitHub
- Kali Linux

## Project Structure

SentinelParser/
├── logs/
├── reports/
├── src/
│ └── engine.py
└── README.md

## Sample Output

192.168.1.10: 6 failed login attempts | Severity: HIGH
ALERT: Possible Brute Force Attack Detected

172.16.1.25: 1 failed login attempts | Severity: LOW

## Future Improvements

- Real-time monitoring
- Email alerting
- Dashboard visualization
- CSV and JSON exports
- Threat intelligence integration

## Author

William Wright II

Cyber & Data Security Technology Student

University of Arizona Global Campus
