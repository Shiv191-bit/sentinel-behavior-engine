from engine.parser import load_logs
from engine.features import extract_features
from model.detector import AnomalyDetector


def show_banner():
    print("=" * 60)
    print("DEFENSIVE SECURITY TOOL")
    print("Sentinel Behavior Engine")
    print("Behavioral Anomaly Detection")
    print("Author: Shivam")
    print("=" * 60)


def main():
    logs = load_logs("data/sample_logs.csv")
    features = extract_features(logs)

    detector = AnomalyDetector(contamination=0.25)
    detector.fit(features)
    results = detector.score(features)

    print(f"\nLoaded {len(logs)} log entries")
    print("Behavioral analysis results:\n")

    for idx, result in enumerate(results, start=1):
        status = "ANOMALY" if result["anomaly"] else "normal"
        print(f"User #{idx}: {status} | score={result['score']:.4f}")


if __name__ == "__main__":
    show_banner()
    main()
