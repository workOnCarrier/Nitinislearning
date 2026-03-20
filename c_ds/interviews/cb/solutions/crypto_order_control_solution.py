"""Deterministic in-memory controller for crypto order states."""
from __future__ import annotations

from typing import Dict


class OrderController:
    """Tracks order states and guards all updates with transition validation."""

    FINAL_STATES = {"CANCELLED", "FILLED"}

    def __init__(self, initial_states: Dict[str, str]):
        self.states = dict(initial_states)

    def pause(self, order_id: str) -> bool:
        return self._transition(order_id, {"ACTIVE"}, "PAUSED")

    def resume(self, order_id: str) -> bool:
        return self._transition(order_id, {"PAUSED"}, "ACTIVE")

    def cancel(self, order_id: str) -> bool:
        return self._transition(order_id, {"ACTIVE", "PAUSED"}, "CANCELLED")

    def state(self, order_id: str) -> str | None:
        return self.states.get(order_id)

    def _transition(self, order_id: str, allowed_from: set[str], target: str) -> bool:
        current = self.states.get(order_id)
        if current is None or current in self.FINAL_STATES:
            return False
        if current not in allowed_from:
            return False
        self.states[order_id] = target
        return True
