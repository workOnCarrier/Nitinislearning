"""Solutions for NFT attribute enumeration and weighted sampling."""
from __future__ import annotations

import random
from itertools import product
from typing import Dict, List


def enumerate_combinations(attributes: Dict[str, List[str]]) -> List[Dict[str, str]]:
    items = sorted(attributes.items())
    if not items:
        return []
    keys, value_lists = zip(*items)
    combos: List[Dict[str, str]] = []
    for values in product(*value_lists):
        combos.append({key: value for key, value in zip(keys, values)})
    return combos


def enumerate_unique_combinations(attributes: Dict[str, List[str]]) -> List[Dict[str, str]]:
    normalized = {key: sorted(set(values)) for key, values in attributes.items()}
    seen = set()
    unique: List[Dict[str, str]] = []
    for combo in enumerate_combinations(normalized):
        key = tuple(sorted(combo.items()))
        if key not in seen:
            seen.add(key)
            unique.append(combo)
    return unique


class WeightedNFTGenerator:
    def __init__(self, weights: Dict[str, Dict[str, float]], seed: int | None = None):
        self.random = random.Random(seed)
        self.distributions = {
            category: _build_distribution(values)
            for category, values in weights.items()
        }

    def generate(self) -> Dict[str, str]:
        selection: Dict[str, str] = {}
        for category, dist in self.distributions.items():
            total, cumulative = dist
            pick = self.random.random() * total
            for value, threshold in cumulative:
                if pick <= threshold:
                    selection[category] = value
                    break
        return selection


def _build_distribution(values: Dict[str, float]) -> tuple[float, List[tuple[str, float]]]:
    total = sum(max(weight, 0.0) for weight in values.values())
    cumulative: List[tuple[str, float]] = []
    running = 0.0
    for value, weight in values.items():
        running += max(weight, 0.0)
        cumulative.append((value, running))
    if total == 0.0:
        total = float(len(values))
        cumulative = []
        running = 0.0
        for idx, value in enumerate(values.keys()):
            running += 1.0
            cumulative.append((value, running))
    return total, cumulative
