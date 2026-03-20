"""Unit tests for calculator_2.evaluate."""
import unittest

from calculator_2 import evaluate


class TestEvaluateValid(unittest.TestCase):
    def test_single_number(self) -> None:
        self.assertEqual(evaluate("5"), 5)

    def test_simple_addition(self) -> None:
        self.assertEqual(evaluate("(2+3)"), 5)

    def test_simple_multiplication(self) -> None:
        self.assertEqual(evaluate("((2+3)*4)"), 20)

    def test_nested_expression(self) -> None:
        expr = "(((1+2)+(3+4))*(5-2))"
        self.assertEqual(evaluate(expr), 30)

    def test_multi_digit_numbers(self) -> None:
        expr = "((12+8)*(3+(4*5)))"
        self.assertEqual(evaluate(expr), 460)

    def test_complex_mixed_operations(self) -> None:
        expr = "(((9-5)*(2+3))+((4*3)-(6-1)))"
        self.assertEqual(evaluate(expr), 27)

    def test_multiple_nested_products(self) -> None:
        expr = "(((1*2)*(3*4))*((5*6)*(7*8)))"
        self.assertEqual(evaluate(expr), 40320)

    def test_large_numbers(self) -> None:
        expr = "(((100+200)-(50+25))*(3*2))"
        self.assertEqual(evaluate(expr), 1350)

    def test_combined_operations(self) -> None:
        expr = "(((8*3)-(2+4))+((1+1)*(3-2)))"
        self.assertEqual(evaluate(expr), 20)


class TestEvaluateErrors(unittest.TestCase):
    def test_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            evaluate("")

    def test_only_whitespace(self) -> None:
        with self.assertRaises(ValueError):
            evaluate("   ")

    def test_missing_closing_parenthesis(self) -> None:
        with self.assertRaises(ValueError):
            evaluate("(2+3")

    def test_missing_operand(self) -> None:
        with self.assertRaises(ValueError):
            evaluate("(2+)")

    def test_invalid_operator(self) -> None:
        with self.assertRaises(ValueError):
            evaluate("(2/3)")

    def test_zero_not_allowed(self) -> None:
        with self.assertRaises(ValueError):
            evaluate("(0+1)")

    def test_negative_literal_not_allowed(self) -> None:
        with self.assertRaises(ValueError):
            evaluate("(-1+2)")

    def test_not_fully_parenthesized(self) -> None:
        with self.assertRaises(ValueError):
            evaluate("2+3")

    def test_trailing_characters(self) -> None:
        with self.assertRaises(ValueError):
            evaluate("((2+3)*4)5")

    def test_missing_operand_right(self) -> None:
        with self.assertRaises(ValueError):
            evaluate("((2+3)*(4+))")

    def test_non_string_input(self) -> None:
        with self.assertRaises(TypeError):
            evaluate(123)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
