"""Practice tests for NFT attribute enumeration and sampling."""
from __future__ import annotations

from typing import Dict, List


def enumerate_combinations(attributes: Dict[str, List[str]]) -> List[Dict[str, str]]:
    """Return the cartesian product of the provided attribute values."""
    raise NotImplementedError


def enumerate_unique_combinations(attributes: Dict[str, List[str]]) -> List[Dict[str, str]]:
    """Return unique attribute combinations even if inputs contain duplicates."""
    raise NotImplementedError


class WeightedNFTGenerator:
    """Samples NFTs according to the per-attribute weight map."""

    def __init__(self, weights: Dict[str, Dict[str, float]], seed: int | None = None):
        raise NotImplementedError

    def generate(self) -> Dict[str, str]:
        raise NotImplementedError


def _run_enumerate(attributes: Dict[str, List[str]]) -> List[Dict[str, str]]:
    try:
        from solutions.nft_attribute_solution import enumerate_combinations as impl
    except ModuleNotFoundError:  # pragma: no cover
        impl = enumerate_combinations
    return impl(attributes)


def _run_unique(attributes: Dict[str, List[str]]) -> List[Dict[str, str]]:
    try:
        from solutions.nft_attribute_solution import enumerate_unique_combinations as impl
    except ModuleNotFoundError:  # pragma: no cover
        impl = enumerate_unique_combinations
    return impl(attributes)


def _make_generator(weights: Dict[str, Dict[str, float]], seed: int | None = None):
    try:
        from solutions.nft_attribute_solution import WeightedNFTGenerator as cls
    except ModuleNotFoundError:  # pragma: no cover
        cls = WeightedNFTGenerator
    return cls(weights, seed=seed)


def test_cartesian_product() -> None:
    attributes = {"Background": ["Red", "Blue"], "Hat": ["Cap", "None"]}
    combos = _run_enumerate(attributes)
    assert len(combos) == 4
    assert {combo["Background"] for combo in combos} == {"Red", "Blue"}
    assert _run_enumerate({}) == []


def test_deduplication() -> None:
    attributes = {"Ears": ["Pointy", "Pointy", "Wide"]}
    combos = _run_unique(attributes)
    assert combos == [{"Ears": "Pointy"}, {"Ears": "Wide"}]
    assert _run_unique({"Color": []}) == []


def test_weighted_sampling_is_deterministic_with_seed() -> None:
    generator = _make_generator(
        {
            "Background": {"Red": 0.7, "Blue": 0.3},
            "Hat": {"Cap": 0.2, "None": 0.8},
        },
        seed=7,
    )
    samples = [generator.generate() for _ in range(3)]
    assert samples[0] == samples[1]
    assert samples[2]["Background"] in {"Red", "Blue"}


def test_weighted_sampling_with_zero_weights() -> None:
    generator = _make_generator({"Eyes": {"Open": 0.0, "Closed": 0.0}}, seed=1)
    sample = generator.generate()
    assert sample["Eyes"] in {"Open", "Closed"}
