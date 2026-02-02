from collections import defaultdict


def extract_features(logs: list) -> list:
    user_stats = defaultdict(lambda: {
        "total": 0,
        "failed": 0,
        "response_time_sum": 0
    })

    for log in logs:
        user = log["user"]
        user_stats[user]["total"] += 1
        user_stats[user]["response_time_sum"] += log["response_time"]

        if log["status"] == "fail":
            user_stats[user]["failed"] += 1

    features = []

    for user, stats in user_stats.items():
        avg_response_time = stats["response_time_sum"] / stats["total"]
        failure_ratio = stats["failed"] / stats["total"]

        features.append([
            stats["total"],        # activity volume
            stats["failed"],       # failed attempts
            failure_ratio,         # failure ratio
            avg_response_time      # avg response time
        ])

    return features
