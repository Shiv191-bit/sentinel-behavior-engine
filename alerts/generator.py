def generate_alert(feature_vector: list, anomaly: bool, score: float) -> dict:
    total, failed, failure_ratio, avg_response = feature_vector

    reasons = []
    confidence = 0

    if failure_ratio > 0.4:
        reasons.append("High login failure ratio")
        confidence += 30

    if failed >= 3:
        reasons.append("Multiple failed login attempts")
        confidence += 25

    if total > 5:
        reasons.append("Unusual login activity volume")
        confidence += 20

    if anomaly:
        confidence += 25

    confidence = min(confidence, 100)

    if confidence >= 70:
        severity = "HIGH"
    elif confidence >= 40:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    return {
        "severity": severity,
        "confidence": confidence,
        "anomaly": anomaly,
        "score": round(score, 4),
        "reasons": reasons
    }
