from engine.parser import load_logs
from engine.features import extract_features
from model.detector import AnomalyDetector
from alerts.generator import generate_alert


def show_banner():
    print("=" * 75)
    print("DEFENSIVE SECURITY TOOL")
    print("Sentinel Behavior Engine")
    print("Behavioral Intrusion Detection & Analyst Guidance")
    print("Author: Shivam")
    print("=" * 75)


def main():
    logs = load_logs("data/sample_logs.csv")
    features = extract_features(logs)

    detector = AnomalyDetector(contamination=0.25)
    detector.fit(features)
    results = detector.score(features)

    print(f"\nLoaded {len(logs)} log entries")
    print("\n=== Actionable Security Alerts ===\n")

    for idx, (feature, result) in enumerate(zip(features, results), start=1):
        alert = generate_alert(
            feature_vector=feature,
            anomaly=result["anomaly"],
            score=result["score"]
        )

        print(f"Entity #{idx}")
        print(f"Severity: {alert['severity']}")
        print(f"Confidence: {alert['confidence']}%")
        print(f"Anomaly: {alert['anomaly']}")
        print(f"Score: {alert['score']}")

        if alert["reasons"]:
            print("Reasons:")
            for r in alert["reasons"]:
                print(f"- {r}")
        else:
            print("Reasons: None")

        if alert["recommended_actions"]:
            print("Recommended Actions:")
            for a in alert["recommended_actions"]:
                print(f"- {a}")
        else:
            print("Recommended Actions: None")

        print("-" * 50)


if __name__ == "__main__":
    show_banner()
    main()
