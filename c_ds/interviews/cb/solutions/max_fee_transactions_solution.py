"""Solutions for the max-fee block assembly problem with and without dependencies."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Sequence, Tuple


@dataclass(frozen=True)
class Transaction:
    tx_id: str
    size: int
    fee: int
    parent_id: str | None = None


def maximize_fee(transactions: Sequence[Transaction], capacity: int) -> Tuple[int, List[str]]:
    n = len(transactions)
    dp = [0] * (capacity + 1)
    choice: List[List[str]] = [[] for _ in range(capacity + 1)]
    for tx in transactions:
        for cap in range(capacity, tx.size - 1, -1):
            candidate = dp[cap - tx.size] + tx.fee
            if candidate > dp[cap]:
                dp[cap] = candidate
                choice[cap] = choice[cap - tx.size] + [tx.tx_id]
    best_cap = max(range(capacity + 1), key=lambda c: dp[c])
    return dp[best_cap], choice[best_cap]


def maximize_fee_with_dependencies(transactions: Sequence[Transaction], capacity: int) -> Tuple[int, List[str]]:
    by_id = {tx.tx_id: tx for tx in transactions}
    children: Dict[str, List[str]] = {tx.tx_id: [] for tx in transactions}
    roots: List[str] = []
    for tx in transactions:
        if tx.parent_id and tx.parent_id in by_id:
            children[tx.parent_id].append(tx.tx_id)
        else:
            roots.append(tx.tx_id)
    combos: List[Tuple[int, int, List[str]]] = []
    for root in roots:
        combos.extend(_enumerate_subtree_combos(root, by_id, children))
    return _knapsack_with_combos(combos, capacity)


def _enumerate_subtree_combos(node_id: str, by_id: Dict[str, Transaction], children: Dict[str, List[str]]) -> List[Tuple[int, int, List[str]]]:
    tx = by_id[node_id]
    combos: List[Tuple[int, int, List[str]]] = [(tx.size, tx.fee, [node_id])]
    for child_id in children.get(node_id, []):
        child_combos = _enumerate_subtree_combos(child_id, by_id, children)
        new_combos = combos.copy()
        for size, fee, nodes in combos:
            for c_size, c_fee, c_nodes in child_combos:
                new_combos.append((size + c_size, fee + c_fee, nodes + c_nodes))
        combos = new_combos
    return combos


def _knapsack_with_combos(combos: List[Tuple[int, int, List[str]]], capacity: int) -> Tuple[int, List[str]]:
    dp = [0] * (capacity + 1)
    choice: List[List[str]] = [[] for _ in range(capacity + 1)]
    for size, fee, nodes in combos:
        for cap in range(capacity, size - 1, -1):
            candidate = dp[cap - size] + fee
            if candidate > dp[cap]:
                dp[cap] = candidate
                choice[cap] = choice[cap - size] + nodes
    best_cap = max(range(capacity + 1), key=lambda c: dp[c])
    return dp[best_cap], choice[best_cap]
