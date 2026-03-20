"""Practice tests for the crypto order state controller."""
from typing import Dict


class OrderController:
    """Tracks in-memory order states and enforces pause/resume/cancel rules."""

    def __init__(self, initial_states: Dict[str, str]):
        raise NotImplementedError

    def pause(self, order_id: str) -> bool:
        raise NotImplementedError

    def resume(self, order_id: str) -> bool:
        raise NotImplementedError

    def cancel(self, order_id: str) -> bool:
        raise NotImplementedError

    def state(self, order_id: str) -> str | None:
        raise NotImplementedError


def make_controller(initial: Dict[str, str]) -> OrderController:
    try:
        from solutions.crypto_order_control_solution import OrderController as controller_cls
    except ModuleNotFoundError:  # pragma: no cover
        controller_cls = OrderController
    return controller_cls(initial)


def test_order_state_transitions() -> None:
    controller = make_controller({
        "alpha": "ACTIVE",
        "beta": "PAUSED",
        "gamma": "FILLED",
    })

    assert controller.pause("alpha") is True
    assert controller.state("alpha") == "PAUSED"

    assert controller.resume("beta") is True
    assert controller.state("beta") == "ACTIVE"

    assert controller.cancel("beta") is True
    assert controller.state("beta") == "CANCELLED"

    # Once cancelled or filled the state must not change.
    assert controller.cancel("beta") is False
    assert controller.pause("gamma") is False
    assert controller.resume("gamma") is False
    assert controller.cancel("gamma") is False


def test_invalid_transitions_and_missing_orders() -> None:
    controller = make_controller({"new": "NEW"})
    assert controller.pause("new") is False  # must be ACTIVE first
    assert controller.resume("new") is False
    assert controller.cancel("unknown") is False
