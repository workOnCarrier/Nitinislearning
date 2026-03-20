"""Solutions for restaurant grid path finding and idempotent order processing."""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Deque, Dict, List, Sequence, Tuple


def shortest_path_to_item(grid: Sequence[str], target_row: int, target_col: int) -> int:
    start = _find_cell(grid, "S")
    if start is None:
        return -1
    return _bfs_distance(grid, start, (target_row, target_col))


def min_steps_collect_all_food(grid: Sequence[str]) -> int:
    start = _find_cell(grid, "S")
    food_cells = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "F"]
    if start is None:
        return -1
    if not food_cells:
        return 0
    points = [start] + food_cells
    distances = [[-1] * len(points) for _ in points]
    for i, point in enumerate(points):
        dists = _bfs_all(grid, point)
        for j, other in enumerate(points):
            distances[i][j] = dists.get(other, -1)
    for idx in range(1, len(points)):
        if distances[0][idx] == -1:
            return -1
    target_mask = (1 << (len(points) - 1)) - 1
    dp: Dict[Tuple[int, int], int] = {}
    for idx in range(1, len(points)):
        mask = 1 << (idx - 1)
        dp[(mask, idx)] = distances[0][idx]
    for mask in range(1, target_mask + 1):
        for idx in range(1, len(points)):
            if not (mask & (1 << (idx - 1))):
                continue
            state = (mask, idx)
            if state not in dp:
                continue
            for nxt in range(1, len(points)):
                if mask & (1 << (nxt - 1)):
                    continue
                dist = distances[idx][nxt]
                if dist == -1:
                    continue
                next_mask = mask | (1 << (nxt - 1))
                best = dp.get((next_mask, nxt))
                cand = dp[state] + dist
                if best is None or cand < best:
                    dp[(next_mask, nxt)] = cand
    best_total = min((dp[(target_mask, idx)] for idx in range(1, len(points)) if (target_mask, idx) in dp), default=-1)
    return best_total


def _find_cell(grid: Sequence[str], target: str) -> Tuple[int, int] | None:
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == target:
                return r, c
    return None


def _bfs_distance(grid: Sequence[str], start: Tuple[int, int], goal: Tuple[int, int]) -> int:
    queue: Deque[Tuple[int, int, int]] = deque([(start[0], start[1], 0)])
    visited = {start}
    rows, cols = len(grid), len(grid[0]) if grid else 0
    while queue:
        r, c, dist = queue.popleft()
        if (r, c) == goal:
            return dist
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#" and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1


def _bfs_all(grid: Sequence[str], start: Tuple[int, int]) -> Dict[Tuple[int, int], int]:
    queue: Deque[Tuple[int, int, int]] = deque([(start[0], start[1], 0)])
    visited = {start}
    rows, cols = len(grid), len(grid[0]) if grid else 0
    dists = {start: 0}
    while queue:
        r, c, dist = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#" and (nr, nc) not in visited:
                visited.add((nr, nc))
                dists[(nr, nc)] = dist + 1
                queue.append((nr, nc, dist + 1))
    return dists


@dataclass
class Event:
    event_id: str
    order_id: str
    type: str
    quantity: int


def process_events(events: List[Event]) -> Dict[str, Dict[str, int | str]]:
    processed = set()
    orders: Dict[str, Dict[str, int | str]] = {}
    for event in events:
        if event.event_id in processed:
            continue
        processed.add(event.event_id)
        order = orders.setdefault(event.order_id, {"state": "", "totalQuantity": 0, "filledQuantity": 0})
        if event.type == "NEW":
            order["state"] = "OPEN"
            order["totalQuantity"] = event.quantity
            order["filledQuantity"] = 0
        elif event.type == "FILL":
            if order["state"] in {"OPEN", "PARTIALLY_FILLED"}:
                order["filledQuantity"] += event.quantity
                if order["filledQuantity"] >= order["totalQuantity"]:
                    order["filledQuantity"] = min(order["filledQuantity"], order["totalQuantity"])
                    order["state"] = "FILLED"
                else:
                    order["state"] = "PARTIALLY_FILLED"
        elif event.type == "CANCEL":
            if order["state"] in {"OPEN", "PARTIALLY_FILLED"}:
                order["state"] = "CANCELLED"
        if not order["state"]:
            order["state"] = "OPEN"
    return orders
