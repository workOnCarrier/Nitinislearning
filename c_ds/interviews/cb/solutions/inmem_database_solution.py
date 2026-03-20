"""Solution for the time-aware in-memory key-value database."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Record:
    value: str
    written_at: int
    expire_at: int | None

    def alive_at(self, timestamp: int) -> bool:
        if timestamp < self.written_at:
            return False
        if self.expire_at is None:
            return True
        return timestamp < self.expire_at


class TimeTravelKV:
    def __init__(self) -> None:
        self.data: Dict[str, Record] = {}
        self.backups: Dict[str, Dict[str, Record]] = {}
        self.backup_seq = 0

    def put(self, key: str, value: str, timestamp: int, ttl_seconds: int | None = None) -> None:
        expire_at = None if ttl_seconds is None else timestamp + ttl_seconds
        self.data[key] = Record(value=value, written_at=timestamp, expire_at=expire_at)

    def get(self, key: str, timestamp: int) -> str | None:
        record = self.data.get(key)
        if not record or not record.alive_at(timestamp):
            return None
        return record.value

    def scan(self, prefix: str, timestamp: int) -> List[Tuple[str, str]]:
        alive_items = [
            (key, record.value)
            for key, record in self.data.items()
            if key.startswith(prefix) and record.alive_at(timestamp)
        ]
        alive_items.sort(key=lambda item: item[0])
        return alive_items

    def backup(self, timestamp: int) -> str:
        snapshot: Dict[str, Record] = {}
        for key, record in self.data.items():
            if record.alive_at(timestamp):
                snapshot[key] = Record(record.value, record.written_at, record.expire_at)
        self.backup_seq += 1
        backup_id = f"backup-{self.backup_seq}"
        self.backups[backup_id] = snapshot
        return backup_id

    def restore(self, backup_id: str, timestamp: int) -> None:  # noqa: ARG002
        snapshot = self.backups.get(backup_id)
        if snapshot is None:
            return
        self.data = {
            key: Record(record.value, record.written_at, record.expire_at)
            for key, record in snapshot.items()
        }
