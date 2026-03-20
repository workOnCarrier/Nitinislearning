"""Solutions for local maxima, bagging classifier, and k-means."""
from __future__ import annotations

import math
import random
from collections import Counter
from typing import List, Sequence, Tuple


def find_local_maxima(values: Sequence[int]) -> List[int]:
    n = len(values)
    if n == 0:
        return []
    maxima: List[int] = []
    for i in range(n):
        left_ok = i == 0 or values[i] > values[i - 1]
        right_ok = i == n - 1 or values[i] > values[i + 1]
        if left_ok and right_ok:
            maxima.append(i)
    return maxima


class BaggingClassifier:
    def __init__(self, base_cls, n_estimators: int = 5, sample_size: int | None = None, random_seed: int = 0):
        self.base_cls = base_cls
        self.n_estimators = n_estimators
        self.sample_size = sample_size
        self.random = random.Random(random_seed)
        self.estimators: List[object] = []

    def fit(self, X: Sequence[Sequence[float]], y: Sequence[int]) -> None:
        n = len(X)
        if n == 0:
            self.estimators = []
            return
        size = self.sample_size or n
        self.estimators = []
        for _ in range(self.n_estimators):
            indices = [self.random.randrange(n) for _ in range(size)]
            sample_X = [X[i] for i in indices]
            sample_y = [y[i] for i in indices]
            estimator = self.base_cls()
            estimator.fit(sample_X, sample_y)
            self.estimators.append(estimator)

    def predict(self, X: Sequence[Sequence[float]]) -> List[int]:
        if not self.estimators:
            return []
        votes_per_estimator = [est.predict(X) for est in self.estimators]
        results: List[int] = []
        for col in zip(*votes_per_estimator):
            counts = Counter(col)
            # Break ties with smallest label.
            best_label, best_count = None, -1
            for label, count in sorted(counts.items()):
                if count > best_count:
                    best_label, best_count = label, count
            results.append(best_label if best_label is not None else 0)
        return results


def kmeans(X: Sequence[Sequence[float]], k: int, max_iter: int = 100) -> Tuple[List[List[float]], List[int]]:
    n = len(X)
    if n == 0 or k <= 0 or k > n:
        return [], []
    centroids = [list(X[i]) for i in range(k)]
    assignments = [0] * n
    for _ in range(max_iter):
        updated_assignments: List[int] = []
        for point in X:
            best_idx = 0
            best_dist = math.inf
            for idx, centroid in enumerate(centroids):
                dist = _squared_distance(point, centroid)
                if dist < best_dist or (math.isclose(dist, best_dist) and idx < best_idx):
                    best_idx = idx
                    best_dist = dist
            updated_assignments.append(best_idx)
        if updated_assignments == assignments:
            break
        assignments = updated_assignments
        cluster_sums = [[0.0] * len(X[0]) for _ in range(k)]
        counts = [0] * k
        for point, idx in zip(X, assignments):
            counts[idx] += 1
            for dim, value in enumerate(point):
                cluster_sums[idx][dim] += value
        for idx in range(k):
            if counts[idx] == 0:
                continue
            centroids[idx] = [val / counts[idx] for val in cluster_sums[idx]]
    return centroids, assignments


def _squared_distance(p: Sequence[float], q: Sequence[float]) -> float:
    return sum((a - b) ** 2 for a, b in zip(p, q))
