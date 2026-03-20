"""Simple broker simulator that exposes an iterable execution stream."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Iterator, List


@dataclass(frozen=True)
class Order:
    order_id: str
    symbol: str
    side: str
    quantity: int
    limit_price: float


@dataclass(frozen=True)
class ExecutionEvent:
    order_id: str
    symbol: str
    side: str
    fill_size: int
    remaining: int
    price: float
    is_complete: bool


class Broker:
    """Simulates a broker that streams partial order executions."""

    def __init__(self, orders: Iterable[Order], fill_size: int = 100) -> None:
        self._orders: List[Order] = list(orders)
        if fill_size <= 0:
            raise ValueError("fill_size must be positive")
        self.fill_size = fill_size
        self._current_order_idx: int = 0
        self._remaining_in_order: int | None = None

    def __iter__(self) -> Iterator[ExecutionEvent]:
        self._current_order_idx = 0
        self._remaining_in_order = None
        return self

    def __next__(self) -> ExecutionEvent:
        while self._current_order_idx < len(self._orders):
            order = self._orders[self._current_order_idx]
            if self._remaining_in_order is None:
                self._remaining_in_order = order.quantity

            remaining_before_fill = self._remaining_in_order
            if remaining_before_fill == 0:
                self._current_order_idx += 1
                self._remaining_in_order = None
                continue

            fill = min(self.fill_size, remaining_before_fill)
            remaining_after_fill = remaining_before_fill - fill
            self._remaining_in_order = remaining_after_fill
            is_complete = remaining_after_fill == 0
            price = self._price_for_fill(order, fill, remaining_after_fill)

            if is_complete:
                self._current_order_idx += 1
                self._remaining_in_order = None

            return ExecutionEvent(
                order_id=order.order_id,
                symbol=order.symbol,
                side=order.side,
                fill_size=fill,
                remaining=remaining_after_fill,
                price=price,
                is_complete=is_complete,
            )

        raise StopIteration

    def _price_for_fill(self, order: Order, fill_size: int, remaining: int) -> float:
        """Deterministic pseudo-slippage to mimic market impact."""
        direction = 1 if order.side.upper() == "BUY" else -1
        progress = (order.quantity - remaining) / order.quantity
        slippage = 0.02 * direction * progress
        return round(order.limit_price + slippage, 2)


def _build_sample_orders() -> List[Order]:
    return [
        Order(order_id="ORD-001", symbol="AAPL", side="BUY", quantity=150, limit_price=187.3),
        Order(order_id="ORD-002", symbol="MSFT", side="SELL", quantity=200, limit_price=342.8),
        Order(order_id="ORD-003", symbol="TSLA", side="BUY", quantity=90, limit_price=252.5),
    ]


def main() -> None:
    broker = Broker(_build_sample_orders(), fill_size=70)
    print("Streaming executions from broker:\n")
    for event in broker:
        print(
            f"{event.order_id} {event.side:4} {event.symbol} filled {event.fill_size:3} @ {event.price:.2f}"
            f" | remaining: {event.remaining:3} | completed: {event.is_complete}"
        )


if __name__ == "__main__":
    main()
