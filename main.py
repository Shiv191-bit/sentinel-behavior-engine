from engine.parser import load_logs
from engine.features import extract_features


def show_banner():
    print("=" * 55)
    print("DEFENSIVE SECURITY TOOL")
    print("Sentinel Behavior Engine")
    print("Author: Shivam")
    print("=" * 55)


def main():
    logs = load_logs("data/sample_logs.csv")
    features = extract_features(logs)

    print(f"\nLoaded {len(logs)} log entries")
    print("Extracted behavioral feature vectors:")

    for vector in features:
        print(vector)


if __name__ == "__main__":
    show_banner()
    main()
