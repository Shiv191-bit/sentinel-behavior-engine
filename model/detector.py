from sklearn.ensemble import IsolationForest
import numpy as np


class AnomalyDetector:
    def __init__(self, contamination: float = 0.2, random_state: int = 42):
        self.model = IsolationForest(
            n_estimators=200,
            contamination=contamination,
            random_state=random_state
        )

    def fit(self, features: list):
        X = np.array(features)
        self.model.fit(X)

    def score(self, features: list) -> list:
        X = np.array(features)
        scores = self.model.decision_function(X)  # higher = more normal
        preds = self.model.predict(X)              # -1 anomaly, 1 normal

        results = []
        for s, p in zip(scores, preds):
            results.append({
                "anomaly": True if p == -1 else False,
                "score": float(s)
            })
        return results
