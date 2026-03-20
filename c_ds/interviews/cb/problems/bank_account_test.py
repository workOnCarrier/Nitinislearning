"""Practice tests for the in-memory banking command processor."""
from typing import Any, Dict, List, Tuple


Command = Dict[str, Any]
Output = Tuple[str, Any]


def process_bank_commands(commands: List[Command]) -> List[Output]:
    """Process commands sorted by timestamp and yield outputs for query commands."""
    raise NotImplementedError("Implement banking system command processor")


def _run(commands: List[Command]) -> List[Output]:
    try:
        from solutions.bank_account_solution import process_bank_commands as implementation
    except ModuleNotFoundError:  # pragma: no cover - reference solutions absent
        implementation = process_bank_commands
    return implementation(commands)


def test_transfers_scheduling_and_merges() -> None:
    commands: List[Command] = [
        {"ts": 1, "op": "CREATE", "account": "alice"},
        {"ts": 2, "op": "CREATE", "account": "bob"},
        {"ts": 3, "op": "DEPOSIT", "account": "alice", "amount": 200},
        {"ts": 4, "op": "TRANSFER", "from": "alice", "to": "bob", "amount": 50},
        {"ts": 5, "op": "TOP_SPENDERS", "k": 2},
        {
            "ts": 6,
            "op": "SCHEDULE_PAYMENT",
            "payment_id": "auto1",
            "from": "alice",
            "to": "bob",
            "amount": 60,
            "execute_at": 8,
        },
        {
            "ts": 6,
            "op": "SCHEDULE_PAYMENT",
            "payment_id": "auto2",
            "from": "alice",
            "to": "bob",
            "amount": 20,
            "execute_at": 12,
        },
        {"ts": 7, "op": "BALANCE", "account": "alice"},
        {"ts": 8, "op": "BALANCE", "account": "bob"},
        {"ts": 9, "op": "CANCEL_PAYMENT", "payment_id": "auto2"},
        {"ts": 10, "op": "MERGE", "target": "alice", "source": "bob"},
        {"ts": 11, "op": "BALANCE", "account": "alice"},
    ]

    outputs = _run(commands)
    assert outputs == [
        ("TOP_SPENDERS", [("alice", 50), ("bob", 0)]),
        ("BALANCE", ("alice", 150)),
        ("BALANCE", ("bob", 110)),
        ("BALANCE", ("alice", 200)),
    ]


def test_idempotent_merge_and_failed_operations() -> None:
    commands = [
        {"ts": 1, "op": "CREATE", "account": "alice"},
        {"ts": 1, "op": "CREATE", "account": "alice"},  # duplicate create ignored
        {"ts": 2, "op": "CREATE", "account": "bob"},
        {"ts": 3, "op": "TRANSFER", "from": "alice", "to": "bob", "amount": 999},  # insufficient
        {"ts": 4, "op": "DEPOSIT", "account": "alice", "amount": 100},
        {
            "ts": 5,
            "op": "SCHEDULE_PAYMENT",
            "payment_id": "p1",
            "from": "alice",
            "to": "bob",
            "amount": 200,
            "execute_at": 8,
        },
        {"ts": 6, "op": "MERGE", "target": "bob", "source": "alice"},
        {"ts": 7, "op": "BALANCE", "account": "bob"},
        {"ts": 9, "op": "BALANCE", "account": "bob"},
    ]

    outputs = _run(commands)
    # Scheduled payment should fail (insufficient) but merge keeps balances additive.
    assert outputs == [
        ("BALANCE", ("bob", 100)),
        ("BALANCE", ("bob", 100)),
    ]
