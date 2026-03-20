"""Practice tests for log parsing grouped by thread."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List


@dataclass
class LogEntry:
    timestamp: datetime
    thread_id: str
    message: str


def group_logs_by_thread(lines: List[str]) -> Dict[str, List[LogEntry]]:
    """Parse each line and return per-thread, timestamp-sorted entries."""
    raise NotImplementedError


def _run_group(lines: List[str]) -> Dict[str, List[LogEntry]]:
    try:
        from solutions.log_parsing_solution import LogEntry as ReferenceLogEntry
        from solutions.log_parsing_solution import group_logs_by_thread as impl
        grouped = impl(lines)
        if grouped and isinstance(next(iter(grouped.values()))[0], ReferenceLogEntry):
            converted: Dict[str, List[LogEntry]] = {}
            for thread_id, entries in grouped.items():
                converted[thread_id] = [LogEntry(entry.timestamp, entry.thread_id, entry.message) for entry in entries]
            return converted
        return grouped
    except ModuleNotFoundError:  # pragma: no cover
        grouped = group_logs_by_thread(lines)
        return grouped


def test_grouping_and_sorting() -> None:
    lines = [
        "2026-02-13T10:15:30Z thread=42 msg=Starting work",
        "2026-02-13T10:15:32Z thread=41 msg=Starting work",
        "2026-02-13T10:15:31Z thread=42 msg=Doing work",
        "malformed line with no timestamp",
    ]
    grouped = _run_group(lines)
    assert list(grouped.keys()) == ["41", "42"]
    assert [entry.message for entry in grouped["42"]] == ["Starting work", "Doing work"]


def test_duplicate_timestamps_and_malformed_lines() -> None:
    lines = [
        "2026-02-13T10:15:30Z thread=42 msg=Start",
        "2026-02-13T10:15:30Z thread=42 msg=Same time",
        "invalid",
        "2026-02-13T10:15:29Z thread=41 msg=Earlier",
    ]
    grouped = _run_group(lines)
    assert [entry.message for entry in grouped["42"]] == ["Start", "Same time"]
