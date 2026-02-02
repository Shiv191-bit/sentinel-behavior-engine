def generate_alert(feature_vector: list, anomaly: bool, score: float) -> dict:
    total, failed, failure_ratio, avg_response = feature_vector

    reasons = []

    if failure_ratio > 0.4:
        reasons.append("High login failure ratio")

    if failed >= 3:
        reasons.append("Multiple failed login attempts")

    if total > 5:
        reasons.append("Unusual login activity volume")

    if anomaly and score < -0.15:
        severity = "HIGH"
    elif anomaly:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    return {
        "severity": severity,
        "anomaly": anomaly,
        "score": round(score, 4),
        "reasons": reasons
    }
