"""Fully parenthesized integer expression evaluator.

Implements the requirements from readme.md:
- supported operators: +, -, *
- expressions must be fully parenthesized
- numbers must be positive integers
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

_OPERATORS: dict[str, Callable[[int, int], int]] = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}


@dataclass
class _Parser:
    expression: str

    def __post_init__(self) -> None:
        self._length = len(self.expression)
        self._index = 0

    def parse(self) -> int:
        value = self._parse_expr()
        if self._index != self._length:
            raise ValueError("Unexpected trailing characters in expression")
        return value

    def _parse_expr(self) -> int:
        if self._index >= self._length:
            raise ValueError("Unexpected end of expression")

        current = self.expression[self._index]
        if current == '(':
            self._index += 1
            left = self._parse_expr()

            if self._index >= self._length:
                raise ValueError("Missing operator in expression")
            operator = self.expression[self._index]
            if operator not in _OPERATORS:
                raise ValueError(f"Unsupported operator '{operator}'")
            self._index += 1

            right = self._parse_expr()

            if self._index >= self._length or self.expression[self._index] != ')':
                raise ValueError("Missing closing parenthesis")
            self._index += 1
            return _OPERATORS[operator](left, right)

        if current.isdigit():
            return self._parse_number()

        raise ValueError(f"Invalid token '{current}' in expression")

    def _parse_number(self) -> int:
        start = self._index
        while self._index < self._length and self.expression[self._index].isdigit():
            self._index += 1
        number = int(self.expression[start:self._index])
        if number <= 0:
            raise ValueError("Only positive integers are allowed")
        return number


def evaluate(expression: str) -> int:
    """Evaluate a fully parenthesized arithmetic expression."""
    if not isinstance(expression, str):
        raise TypeError("Expression must be provided as a string")
    expression = expression.strip()
    if not expression:
        raise ValueError("Expression cannot be empty")
    parser = _Parser(expression)
    return parser.parse()



def commandline():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python calculator_2.py '<expression>'")
        raise SystemExit(1)
    try:
        print(evaluate(sys.argv[1]))
    except ValueError as exc:
        print(f"Invalid expression: {exc}")
        raise SystemExit(2)





def test_1():
    input = "5"
    expected_output = 5
    print(evaluate(input))
    print(evaluate("(2+3)"))
    print(evaluate("((2+3)*4)"))
    print(evaluate("(5*(2+3))"))
    print(evaluate("((5-3)*(2+3))"))


if __name__ == "__main__":
    test_1()