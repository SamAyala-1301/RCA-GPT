# RCA-GPT

AI-powered root cause assistant for support engineers.---

## ✅ PHASE 1: LOG MONITORING SYSTEM (COMPLETED)

This phase recreated the basics of how logs are generated, monitored, and alerted on in a production support environment.

### 🔹 1. Log Generator (Simulated)
We wrote a script to simulate a real application producing logs in real time. It writes random log entries (INFO, WARN, ERROR) every 2 seconds to a file.

### 🔹 2. Error Monitor
Another script checks the most recent log entries for spikes in `ERROR`s. If too many are found, it writes a timestamped alert to an alert log — mimicking how tools like Splunk or CloudWatch trigger alarms.

### 🔹 3. Automation via Cron
The monitoring script is scheduled to run every minute using a `cron` job, making the process automated like it would be in production systems.

### 🔹 4. Real-Time Observation
Used `tail -f` to observe live logs from the terminal, simulating an engineer monitoring a live system under pressure.

---
