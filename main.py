from engine.parser import load_logs
from engine.features import extract_features


def show_banner():
    print("=" * 55)
    print("DEFENSIVE SECURITY TOOL")
    print("Behavioral Intrusion Detection Engine")
    print("Author: Shivam")
    print("=" * 55)


if __name__ == "__main__":
    show_banner()

    logs = load_logs("data/sample_logs.csv")
    features = extract_features(logs)

    print(f"\nLoaded {len(logs)} log entries")
    print("Feature samples:")
    for f in features[:3]:
        print(f)
