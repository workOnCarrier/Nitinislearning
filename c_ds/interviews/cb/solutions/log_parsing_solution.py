"""Solution for parsing logs by thread ID and timestamp."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
import re
from typing import Dict, List


@dataclass
class LogEntry:
    timestamp: datetime
    thread_id: str
    message: str


LOG_PATTERN = re.compile(r"^(?P<ts>\S+)\s+thread=(?P<thread>\S+)\s+msg=(?P<msg>.+)$")


def group_logs_by_thread(lines: List[str]) -> Dict[str, List[LogEntry]]:
    grouped: Dict[str, List[LogEntry]] = defaultdict(list)
    for line in lines:
        match = LOG_PATTERN.match(line.strip())
        if not match:
            continue
        ts_raw = match.group("ts")
        try:
            timestamp = _parse_timestamp(ts_raw)
        except ValueError:
            continue
        grouped[match.group("thread")].append(
            LogEntry(timestamp=timestamp, thread_id=match.group("thread"), message=match.group("msg"))
        )
    ordered: Dict[str, List[LogEntry]] = {}
    for thread_id in sorted(grouped.keys()):
        ordered[thread_id] = sorted(grouped[thread_id], key=lambda entry: entry.timestamp)
    return ordered


def _parse_timestamp(raw: str) -> datetime:
    if raw.endswith("Z"):
        raw = raw[:-1] + "+00:00"
    return datetime.fromisoformat(raw)
