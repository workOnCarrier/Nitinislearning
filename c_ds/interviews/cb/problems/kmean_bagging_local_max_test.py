"""Practice problems for array local maxima, bagging, and k-means."""
from __future__ import annotations

from typing import List, Sequence, Tuple


def find_local_maxima(values: Sequence[int]) -> List[int]:
    """Return indices of local maxima according to the interview spec."""
    raise NotImplementedError


class BaggingClassifier:
    """Bagging ensemble that bootstraps base estimators and votes."""

    def __init__(self, base_cls, n_estimators: int = 5, sample_size: int | None = None, random_seed: int = 0):
        raise NotImplementedError

    def fit(self, X: Sequence[Sequence[float]], y: Sequence[int]) -> None:
        raise NotImplementedError

    def predict(self, X: Sequence[Sequence[float]]) -> List[int]:
        raise NotImplementedError


def kmeans(X: Sequence[Sequence[float]], k: int, max_iter: int = 100) -> Tuple[List[List[float]], List[int]]:
    """Run k-means with deterministic initialization (first k points)."""
    raise NotImplementedError


def _run_find_local_maxima(values: Sequence[int]) -> List[int]:
    try:
        from solutions.kmean_bagging_local_max_solution import find_local_maxima as impl
    except ModuleNotFoundError:  # pragma: no cover
        impl = find_local_maxima
    return impl(values)


def _make_bagging(*args, **kwargs):
    try:
        from solutions.kmean_bagging_local_max_solution import BaggingClassifier as cls
    except ModuleNotFoundError:  # pragma: no cover
        cls = BaggingClassifier
    return cls(*args, **kwargs)


def _run_kmeans(X: Sequence[Sequence[float]], k: int, max_iter: int = 100):
    try:
        from solutions.kmean_bagging_local_max_solution import kmeans as impl
    except ModuleNotFoundError:  # pragma: no cover
        impl = kmeans
    return impl(X, k, max_iter)


class ThresholdStump:
    """Tiny 1-D stump used by the tests to validate bagging behavior."""

    def __init__(self) -> None:
        self.threshold = 0.0

    def fit(self, X: Sequence[Sequence[float]], y: Sequence[int]) -> None:
        candidates = sorted(zip(X, y), key=lambda pair: pair[0][0])
        best_threshold = candidates[0][0][0]
        best_err = len(candidates) + 1
        for value, _ in candidates:
            threshold = value[0]
            predictions = [1 if row[0] >= threshold else 0 for row, _ in candidates]
            err = sum(pred != label for pred, (_, label) in zip(predictions, candidates))
            if err < best_err:
                best_err = err
                best_threshold = threshold
        self.threshold = best_threshold

    def predict(self, X: Sequence[Sequence[float]]) -> List[int]:
        return [1 if row[0] >= self.threshold else 0 for row in X]


def test_find_local_maxima() -> None:
    assert _run_find_local_maxima([1, 3, 2, 3, 5, 4, 4]) == [1, 4]
    assert _run_find_local_maxima([5]) == [0]
    assert _run_find_local_maxima([]) == []


def test_bagging_classifier_majority_vote() -> None:
    X = [[0.0], [1.0], [2.0], [3.0], [4.0]]
    y = [0, 0, 0, 1, 1]
    clf = _make_bagging(ThresholdStump, n_estimators=5, sample_size=4, random_seed=42)
    clf.fit(X, y)
    assert clf.predict([[0.5], [3.5], [1.5]]) == [0, 1, 0]

    tie_clf = _make_bagging(ThresholdStump, n_estimators=1, sample_size=1, random_seed=0)
    tie_clf.estimators = []  # predicting without fitting returns empty
    assert tie_clf.predict([[1.0]]) == []


def test_kmeans_two_clusters() -> None:
    points = [[0.0, 0.0], [0.0, 1.0], [5.0, 5.0], [5.0, 6.0]]
    centroids, assignments = _run_kmeans(points, k=2, max_iter=10)
    assert assignments in ([0, 0, 1, 1], [1, 1, 0, 0])
    assert len(centroids) == 2


def test_kmeans_handles_single_cluster() -> None:
    points = [[1.0, 2.0], [2.0, 3.0]]
    centroids, assignments = _run_kmeans(points, k=1, max_iter=5)
    assert assignments == [0, 0]
    assert len(centroids) == 1
