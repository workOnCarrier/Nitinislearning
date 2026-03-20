"""Solution for the in-memory banking command processor.

The processor keeps per-account balances/outgoing-spend, tracks scheduled payments
with a min-heap keyed by execute_at, and emits outputs for query commands. All
commands are executed in timestamp order, and scheduled payments fire the moment
we advance the clock beyond their execute_at provided sufficient funds exist.

Design choices
- CREATE of an existing account is ignored to keep behavior deterministic.
- Invalid transfers/payments (missing accounts or insufficient balance) are
  skipped, just as many banking OAs define.
- Scheduled payments referencing a merged source account are re-pointed to the
  merge target so outstanding obligations still clear predictably.
"""
from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Any, Dict, List, Tuple

Command = Dict[str, Any]
Output = Tuple[str, Any]


@dataclass
class Payment:
    payment_id: str
    from_id: str
    to_id: str
    amount: int
    execute_at: int
    canceled: bool = False


class BankEngine:
    def __init__(self) -> None:
        self.accounts: Dict[str, Dict[str, int]] = {}
        self.payments: Dict[str, Payment] = {}
        self.payment_heap: List[Tuple[int, str]] = []

    def process(self, commands: List[Command]) -> List[Output]:
        outputs: List[Output] = []
        for command in sorted(commands, key=lambda c: c["ts"]):
            self._execute_due_payments(command["ts"])
            result = self._apply(command)
            if result is not None:
                outputs.append(result)
        return outputs

    def _execute_due_payments(self, current_ts: int) -> None:
        while self.payment_heap and self.payment_heap[0][0] <= current_ts:
            execute_at, payment_id = heappop(self.payment_heap)
            payment = self.payments.get(payment_id)
            if not payment or payment.canceled:
                continue
            self._apply_payment(payment)
            payment.canceled = True  # Prevent re-processing.

    def _apply_payment(self, payment: Payment) -> None:
        src = self.accounts.get(payment.from_id)
        dst = self.accounts.get(payment.to_id)
        if not src or not dst:
            return
        if src["balance"] < payment.amount:
            return
        src["balance"] -= payment.amount
        src["spend"] += payment.amount
        dst["balance"] += payment.amount

    def _apply(self, command: Command) -> Output | None:
        op = command["op"]
        if op == "CREATE":
            self.accounts.setdefault(command["account"], {"balance": 0, "spend": 0})
        elif op == "DEPOSIT":
            account = self.accounts.get(command["account"])
            if account:
                account["balance"] += int(command["amount"])
        elif op == "TRANSFER":
            self._transfer(command)
        elif op == "TOP_SPENDERS":
            k = int(command.get("k", 0))
            ranking = sorted(
                ((acc_id, info["spend"]) for acc_id, info in self.accounts.items()),
                key=lambda pair: (-pair[1], pair[0]),
            )
            return ("TOP_SPENDERS", ranking[:k])
        elif op == "SCHEDULE_PAYMENT":
            self._schedule_payment(command)
        elif op == "CANCEL_PAYMENT":
            payment = self.payments.get(command["payment_id"])
            if payment:
                payment.canceled = True
        elif op == "MERGE":
            self._merge_accounts(command)
        elif op == "BALANCE":
            account = command["account"]
            balance = self.accounts.get(account, {"balance": 0})["balance"]
            return ("BALANCE", (account, balance))
        return None

    def _transfer(self, command: Command) -> None:
        src = self.accounts.get(command["from"])
        dst = self.accounts.get(command["to"])
        amount = int(command.get("amount", 0))
        if not src or not dst or amount < 0:
            return
        if src["balance"] < amount:
            return
        src["balance"] -= amount
        dst["balance"] += amount
        src["spend"] += amount

    def _schedule_payment(self, command: Command) -> None:
        payment_id = command["payment_id"]
        if payment_id in self.payments:
            return
        payment = Payment(
            payment_id=payment_id,
            from_id=command["from"],
            to_id=command["to"],
            amount=int(command["amount"]),
            execute_at=int(command["execute_at"]),
        )
        self.payments[payment_id] = payment
        heappush(self.payment_heap, (payment.execute_at, payment.payment_id))

    def _merge_accounts(self, command: Command) -> None:
        target_id = command["target"]
        source_id = command["source"]
        if target_id == source_id:
            return
        target = self.accounts.setdefault(target_id, {"balance": 0, "spend": 0})
        source = self.accounts.get(source_id)
        if not source:
            return
        target["balance"] += source["balance"]
        target["spend"] += source["spend"]
        del self.accounts[source_id]
        for payment in self.payments.values():
            if payment.canceled:
                continue
            if payment.from_id == source_id:
                payment.from_id = target_id
            if payment.to_id == source_id:
                payment.to_id = target_id


def process_bank_commands(commands: List[Command]) -> List[Output]:
    return BankEngine().process(commands)
