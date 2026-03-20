"""Practice tests for restaurant grid paths and order event processing."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


def shortest_path_to_item(grid: List[str], target_row: int, target_col: int) -> int:
    """Return the length of the shortest path from S to the target food cell."""
    raise NotImplementedError


def min_steps_collect_all_food(grid: List[str]) -> int:
    """Return the minimum steps needed to collect all F cells, or -1 if impossible."""
    raise NotImplementedError


@dataclass
class Event:
    event_id: str
    order_id: str
    type: str
    quantity: int


def process_events(events: List[Event]) -> Dict[str, Dict[str, int | str]]:
    """Process events idempotently and return per-order final states."""
    raise NotImplementedError


def _run_shortest_path(grid: List[str], row: int, col: int) -> int:
    try:
        from solutions.restaurant_path_solution import shortest_path_to_item as impl
    except ModuleNotFoundError:  # pragma: no cover
        impl = shortest_path_to_item
    return impl(grid, row, col)


def _run_collect_all(grid: List[str]) -> int:
    try:
        from solutions.restaurant_path_solution import min_steps_collect_all_food as impl
    except ModuleNotFoundError:  # pragma: no cover
        impl = min_steps_collect_all_food
    return impl(grid)


def _run_process_events(events: List[Event]) -> Dict[str, Dict[str, int | str]]:
    try:
        from solutions.restaurant_path_solution import Event as ReferenceEvent
        from solutions.restaurant_path_solution import process_events as impl
        converted = [ReferenceEvent(e.event_id, e.order_id, e.type, e.quantity) for e in events]
        return impl(converted)
    except ModuleNotFoundError:  # pragma: no cover
        return process_events(events)


def test_shortest_paths() -> None:
    grid = [
        "S.F",
        ".#.",
        "..F",
    ]
    assert _run_shortest_path(grid, 0, 2) == 2
    assert _run_collect_all(grid) == 4


def test_order_processing_with_duplicates() -> None:
    events = [
        Event("e1", "o1", "NEW", 5),
        Event("e2", "o1", "FILL", 3),
        Event("e2", "o1", "FILL", 3),  # duplicate
        Event("e3", "o1", "CANCEL", 0),
        Event("e4", "o2", "NEW", 2),
        Event("e5", "o2", "FILL", 2),
    ]
    result = _run_process_events(events)
    assert result["o1"]["state"] == "CANCELLED"
    assert result["o1"]["filledQuantity"] == 3
    assert result["o2"]["state"] == "FILLED"


def test_unreachable_and_no_food_cases() -> None:
    grid = [
        "S#F",
        "###",
        "..F",
    ]
    assert _run_shortest_path(grid, 0, 2) == -1
    assert _run_collect_all(["S.."]) == 0


def test_event_processing_after_final_state() -> None:
    events = [
        Event("e1", "o1", "NEW", 2),
        Event("e2", "o1", "FILL", 2),
        Event("e3", "o1", "FILL", 2),  # ignored duplicate and over-fill
        Event("e4", "o1", "CANCEL", 0),
    ]
    result = _run_process_events(events)
    assert result["o1"]["state"] == "FILLED"
    assert result["o1"]["filledQuantity"] == 2
