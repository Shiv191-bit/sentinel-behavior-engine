def extract_features(logs: list) -> list:
    features = []

    for log in logs:
        features.append([
            1 if log["status"] == "fail" else 0,
            log["response_time"]
        ])

    return features
