import csv
from datetime import datetime


def load_logs(path: str) -> list:
    logs = []

    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            logs.append({
                "timestamp": datetime.fromisoformat(row["timestamp"]),
                "user": row["user"],
                "ip": row["ip"],
                "action": row["action"],
                "status": row["status"],
                "response_time": int(row["response_time"])
            })

    return logs
