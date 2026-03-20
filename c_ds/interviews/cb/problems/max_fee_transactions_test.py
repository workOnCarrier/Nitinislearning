"""Practice tests for the max-fee block assembly problem."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class Transaction:
    tx_id: str
    size: int
    fee: int
    parent_id: str | None = None


def maximize_fee(transactions: List[Transaction], capacity: int) -> Tuple[int, List[str]]:
    """Return (total_fee, tx_ids) maximizing fees within capacity."""
    raise NotImplementedError


def maximize_fee_with_dependencies(transactions: List[Transaction], capacity: int) -> Tuple[int, List[str]]:
    """Maximum fee respecting parent/child dependencies."""
    raise NotImplementedError


def _run_maximize(transactions: List[Transaction], capacity: int) -> Tuple[int, List[str]]:
    try:
        from solutions.max_fee_transactions_solution import maximize_fee as impl
    except ModuleNotFoundError:  # pragma: no cover
        impl = maximize_fee
    return impl(transactions, capacity)


def _run_maximize_with_deps(transactions: List[Transaction], capacity: int) -> Tuple[int, List[str]]:
    try:
        from solutions.max_fee_transactions_solution import maximize_fee_with_dependencies as impl
    except ModuleNotFoundError:  # pragma: no cover
        impl = maximize_fee_with_dependencies
    return impl(transactions, capacity)


def test_basic_knapsack() -> None:
    txs = [
        Transaction("a", 2, 100),
        Transaction("b", 1, 19),
        Transaction("c", 3, 27),
        Transaction("d", 2, 25),
    ]
    total, chosen = _run_maximize(txs, capacity=4)
    assert total == 125
    assert set(chosen) == {"a", "d"}


def test_dependency_knapsack() -> None:
    txs = [
        Transaction("root", 3, 70, None),
        Transaction("leaf1", 1, 40, "root"),
        Transaction("leaf2", 1, 30, "root"),
        Transaction("solo", 2, 90, None),
    ]
    total, chosen = _run_maximize_with_deps(txs, capacity=5)
    assert total == 160
    assert set(chosen) == {"root", "solo"}


def test_capacity_zero_and_orphan_dependency() -> None:
    txs = [Transaction("root", 2, 50), Transaction("child", 1, 30, "missing")]
    assert _run_maximize(txs, capacity=0) == (0, [])
    total, chosen = _run_maximize_with_deps(txs, capacity=3)
    assert total == 80
    assert set(chosen) == {"root", "child"}
