# RCA-GPT

AI-powered root cause analysis assistant for support engineers.

## 🚀 Quick Start
```bash
# Install
pip install -r requirements.txt
pip install -e .

# Generate logs (for demo)
bash bash/generate_logs.sh &

# Parse logs
rca-gpt parse

# Train model (requires labeled training data)
rca-gpt train

# Classify incidents
rca-gpt predict "Invalid token"
```

## 📁 Project Structure
```
rca-gpt/
├── rca_gpt/           # Core Python package
│   ├── parser.py      # Log parsing
│   ├── trainer.py     # ML training
│   └── predictor.py   # Classification
├── config/            # Configuration
│   └── config.yaml
├── data/
│   ├── raw/          # Auto-generated logs
│   └── training/     # Labeled training data
├── models/           # Saved ML models
└── cli.py           # Command-line interface
```

## 🎯 Features

### ✅ Phase 1: Log Monitoring (Completed)
- Automated log generation and monitoring
- Pattern-based error detection
- Scheduled monitoring via cron

### ✅ Phase 2: Structured Parsing (Completed)
- Regex-based log parsing
- CSV export for analysis
- Configurable via YAML

### ✅ Phase 3: ML Classification (Completed)
- TF-IDF + Logistic Regression classifier
- Persistent model storage
- Batch and single prediction modes

### ✅ Sprint 0: Foundation (Current)
- **NEW:** Config-driven architecture
- **NEW:** Persistent ML models (no retraining needed)
- **NEW:** Proper Python package structure
- **NEW:** CLI interface
- **FIXED:** Training data preservation

## 🛠️ Usage

### Parse Logs
```bash
# Parse with defaults
rca-gpt parse

# Custom input/output
rca-gpt parse -i logs/custom.log -o data/output.csv

# Append mode
rca-gpt parse --append
```

### Train Model
```bash
# Train from labeled data
rca-gpt train

# Model saved to: models/classifier.pkl
```

### Predict Incidents
```bash
# Single message
rca-gpt predict "Connection refused"

# Batch prediction
echo "Invalid token
Connection timeout
Login failed" > messages.txt

rca-gpt predict -b messages.txt
```

## 📊 Training Data Format

`data/training/training_data.csv`:
```csv
level,timestamp,message,incident_type
ERROR,12/06/25 10:57,Invalid token,Auth Error
WARN,12/06/25 10:57,Connection refused,DB Error
INFO,12/06/25 10:57,Timeout,Timeout
INFO,12/06/25 10:57,Login success,Normal
```

**Supported incident types:**
- `Auth Error` - Authentication/authorization failures
- `Timeout` - Request timeouts
- `DB Error` - Database connection issues
- `Normal` - Successful operations

## 🔧 Configuration

Edit `config/config.yaml` to customize:
- Log file paths
- Monitoring thresholds
- Model parameters
- Data locations

## 🚧 Roadmap for V2

- **Sprint 1:** Incident database (SQLite)
- **Sprint 2:** Similar incident matching
- **Sprint 3:** Timeline analysis
- **Sprint 4:** Pattern mining
- **Sprint 5:** Causality graphs
- **Sprint 6:** Runbook system

## 📝 Version History

- **v1.0 (Sprint 0)** - Foundation cleanup, persistent models, CLI
- **v0.3** - ML-based classification
- **v0.2** - Structured parsing
- **v0.1** - Basic monitoring

## 👨‍💻 Author

Sai Sampath Ayalasomayajula

## 📄 License

MIT License - see LICENSE file