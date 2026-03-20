"""Reference solution for Execute Grid Moves."""
from typing import Tuple


def execute_grid_moves(cmd: str) -> Tuple[int, int]:
    """Simulate the command string (case-insensitive) and return the final (x, y)."""
    moves = {
        "u": (0, 1),
        "d": (0, -1),
        "l": (-1, 0),
        "r": (1, 0),
    }
    x = y = 0
    for ch in cmd.lower():
        dx_dy = moves.get(ch)
        if dx_dy is None:
            continue  # ignore invalid characters
        dx, dy = dx_dy
        x += dx
        y += dy
    return x, y


def _run_tests() -> None:
    tests = [
        ("", (0, 0)),  # no movement
        ("UuDdLlRr", (0, 0)),  # opposite moves cancel, mixed case
        ("rruLL", (0, 1)),  # ending above origin after returning to x=0
        ("r2d", (1, -1)),  # ignore invalid characters like digits
        ("lLluuDR", (-2, 1)),  # ensure left/right/up/down interplay is correct
    ]

    for idx, (cmd, expected) in enumerate(tests, 1):
        result = execute_grid_moves(cmd)
        assert result == expected, f"Test {idx} failed: expected {expected}, got {result}"
    print("All Execute Grid Moves tests passed.")


if __name__ == "__main__":
    _run_tests()
