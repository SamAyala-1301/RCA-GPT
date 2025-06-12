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


## ✅ Phase 2: Structured Log Parser (Python)

- Parses `app.log` into structured rows using Python and regex
- Extracts fields: `timestamp`, `log level`, `message`
- Saves output as `logs/structured_logs.csv`
- Output is used directly as training data for the ML classifier

---

## ✅ Phase 3: Incident Classification (ML)

- Labeled logs using a new `incident_type` column
- Built a classifier using `TfidfVectorizer` + `LogisticRegression`
- Automatically predicts incident types based on message content
- Prints a full classification report (precision, recall, F1-score)
- Examples of supported labels: `Auth Error`, `Timeout`, `DB Error`, `Normal`

> This phase is fully trainable and testable using `incident_classifier.py`.

---

## 🚀 Versioning

This repository is currently at:

**v1.0 – ML-based RCA pipeline**

- Fully working bash + Python incident monitoring
- Generates logs, parses them, and classifies incidents using ML
- Designed to mirror real-world support automation from scratch

---

## 🧠 What's Next (v2.0)

- Integrate GPT/LLM to generate RCA summaries
- Add UI/CLI interface for user-friendly interaction
- Expand incident type taxonomy and classifier

---

## 👨‍💻 Author

**Sai Sampath Ayalasomayajula**  
Built to learn, demonstrate, and automate root cause analysis pipelines using real tools from scratch.