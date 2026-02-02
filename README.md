# Sentinel Behavior Engine

Sentinel Behavior Engine is a defensive security tool designed to analyze
authentication logs and identify suspicious behavior using behavioral analytics
and anomaly detection.

The engine focuses on clarity, explainability, and analyst usability, making it
suitable for real-world security monitoring and investigation workflows.

Author: Shivam

---

## What This Tool Does

Sentinel Behavior Engine processes structured authentication logs and:

- Builds behavioral profiles from user activity
- Detects anomalous behavior using Isolation Forest
- Correlates multiple weak signals into meaningful alerts
- Assigns severity and confidence scores
- Provides clear, actionable guidance for analysts

The goal is not just detection, but decision support.

---

## How Detection Works (High-Level)

1. Authentication logs are parsed from a CSV file
2. Behavioral features are extracted per entity:
   - Activity volume
   - Failed login count
   - Failure ratio
   - Average response time
3. An Isolation Forest model learns baseline behavior
4. Behavioral outliers are identified
5. Alerts are generated with:
   - Severity (LOW / MEDIUM / HIGH)
   - Confidence score
   - Detection reasons
   - Recommended analyst actions

The system prioritizes explainability over black-box detection.

---

## Project Structure
sentinel-behavior-engine/
├── engine/
│   ├── __init__.py
│   ├── parser.py          # Log ingestion & normalization
│   └── features.py        # Behavioral feature extraction
│
├── model/
│   ├── __init__.py
│   └── detector.py        # ML-based anomaly detection engine
│
├── alerts/
│   ├── __init__.py
│   └── generator.py       # Alert scoring & recommendations
│
├── data/
│   └── sample_logs.csv    # Sample behavioral log dataset
│
├── main.py                # Tool entry point (CLI runner)
├── requirements.txt       # Python dependencies
└── README.md              # Documentation & usage guide

---

## System Requirements

- Python 3.9 or newer
- pip
- Virtual environment support

Tested on:
- macOS
- Windows
- Kali Linux
- BlackArch Linux

---

## Installation

### macOS / Kali Linux / BlackArch

```bash
git clone https://github.com/Shiv191-bit/sentinel-behavior-engine.git
cd sentinel-behavior-engine

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

Windows (PowerShell)
git clone https://github.com/Shiv191-bit/sentinel-behavior-engine.git
cd sentinel-behavior-engine

python -m venv .venv
.\.venv\Scripts\activate

pip install -r requirements.txt



Usage
macOS / Linux / Kali / BlackArch

python3 main.py --logfile data/sample_logs.csv
Windows

python main.py --logfile data\sample_logs.csv

Optional Configuration

python3 main.py --logfile data/sample_logs.csv --contamination 0.15
Lower value = stricter detectionHigher value = more aggressive detection

Output
The engine generates structured alerts including:
* Severity level
* Confidence score
* Anomaly indicator
* Detection reasons
* Recommended analyst actions

Log Format
Expected CSV columns:

timestamp,user,ip,action,status,response_time
Example:

2026-02-01T10:00:01,admin,10.0.0.1,login,success,120

Notes
* Designed for structured authentication logs
* Focused on clarity and explainability
* Suitable for SOC analysis and detection engineering
