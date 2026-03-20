"""Fully parenthesized integer expression evaluator.

Implements the requirements from readme.md:
- supported operators: +, -, *
- expressions must be fully parenthesized
- numbers must be positive integers
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Protocol

_OPERATORS: dict[str, Callable[[int, int], int]] = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}


class _Node(Protocol):
    def evaluate(self) -> int:
        """Return the integer value this node represents."""


@dataclass(frozen=True)
class _NumberNode:
    value: int

    def evaluate(self) -> int:
        return self.value


@dataclass(frozen=True)
class _BinaryOpNode:
    operator: str
    left: _Node
    right: _Node

    def evaluate(self) -> int:
        return _OPERATORS[self.operator](self.left.evaluate(), self.right.evaluate())


@dataclass
class _Parser:
    expression: str

    def __post_init__(self) -> None:
        self._length = len(self.expression)
        self._index = 0

    def parse(self) -> _Node:
        node = self._parse_expr()
        self._skip_whitespace()
        if self._index != self._length:
            raise ValueError("Unexpected trailing characters in expression")
        return node

    def _parse_expr(self) -> _Node:
        self._skip_whitespace()
        if self._index >= self._length:
            raise ValueError("Unexpected end of expression")

        current = self.expression[self._index]
        if current == '(':
            self._index += 1
            left = self._parse_expr()
            self._skip_whitespace()

            if self._index >= self._length:
                raise ValueError("Missing operator in expression")
            operator = self.expression[self._index]
            if operator not in _OPERATORS:
                raise ValueError(f"Unsupported operator '{operator}'")
            self._index += 1

            right = self._parse_expr()
            self._skip_whitespace()

            if self._index >= self._length or self.expression[self._index] != ')':
                raise ValueError("Missing closing parenthesis")
            self._index += 1
            return _BinaryOpNode(operator, left, right)

        if current.isdigit():
            return self._parse_number()

        raise ValueError(f"Invalid token '{current}' in expression")

    def _parse_number(self) -> _NumberNode:
        start = self._index
        while self._index < self._length and self.expression[self._index].isdigit():
            self._index += 1
        number = int(self.expression[start:self._index])
        if number <= 0:
            raise ValueError("Only positive integers are allowed")
        return _NumberNode(number)

    def _skip_whitespace(self) -> None:
        while self._index < self._length and self.expression[self._index].isspace():
            self._index += 1


def evaluate(expression: str) -> int:
    """Evaluate a fully parenthesized arithmetic expression."""
    if not isinstance(expression, str):
        raise TypeError("Expression must be provided as a string")
    expression = expression.strip()
    if not expression:
        raise ValueError("Expression cannot be empty")
    parser = _Parser(expression)
    ast = parser.parse()
    return ast.evaluate()



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
