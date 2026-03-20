"""Practice tests for the time-aware in-memory key-value database."""
from typing import List, Tuple


class TimeTravelKV:
    """Supports put/get/scan with TTL and backup + restore."""

    def put(self, key: str, value: str, timestamp: int, ttl_seconds: int | None = None) -> None:  # noqa: D401
        raise NotImplementedError

    def get(self, key: str, timestamp: int) -> str | None:
        raise NotImplementedError

    def scan(self, prefix: str, timestamp: int) -> List[Tuple[str, str]]:
        raise NotImplementedError

    def backup(self, timestamp: int) -> str:
        raise NotImplementedError

    def restore(self, backup_id: str, timestamp: int) -> None:
        raise NotImplementedError


def make_store() -> TimeTravelKV:
    try:
        from solutions.inmem_database_solution import TimeTravelKV as cls
    except ModuleNotFoundError:  # pragma: no cover
        cls = TimeTravelKV
    return cls()


def test_full_lifecycle() -> None:
    store = make_store()
    store.put("alpha", "v1", 1)
    store.put("beta", "v2", 2, ttl_seconds=3)
    store.put("beta2", "v3", 3)

    assert store.get("alpha", 2) == "v1"
    assert store.get("beta", 4) == "v2"
    assert store.get("beta", 6) is None

    assert store.scan("b", 4) == [("beta", "v2"), ("beta2", "v3")]

    backup_id = store.backup(4)
    store.put("alpha", "v4", 5)
    store.put("beta", "v5", 5)
    assert store.get("alpha", 5) == "v4"

    store.restore(backup_id, 10)
    assert store.get("alpha", 11) == "v1"
    assert store.get("beta", 11) is None
    assert store.scan("b", 11) == [("beta2", "v3")]


def test_zero_ttl_and_invalid_restore() -> None:
    store = make_store()
    store.put("temp", "v", 1, ttl_seconds=0)
    assert store.get("temp", 1) is None
    backup_id = store.backup(2)
    assert store.restore("missing", 5) is None
    store.put("persist", "v2", 3)
    store.restore(backup_id, 10)
    assert store.get("persist", 11) is None
