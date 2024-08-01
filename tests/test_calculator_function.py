import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculator.calculator_python import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_validate_expression_valid(self):
        self.calc.expression = "3+5*2-8/4"
        self.assertTrue(self.calc.validate_expression())

    def test_validate_expression_invalid_characters(self):
        self.calc.expression = "3+5*2-8/4a"
        self.assertFalse(self.calc.validate_expression())

    def test_validate_expression_consecutive_operators(self):
        self.calc.expression = "3++5*2"
        self.assertFalse(self.calc.validate_expression())

    def test_evaluate_expression(self):
        self.calc.expression = "3+5*2-8/4"
        result = self.calc.evaluate_expression()
        self.assertEqual(result, 11.0)

    def test_evaluate_expression_with_parentheses(self):
        self.calc.expression = "(3+5)*2"
        result = self.calc.evaluate_expression()
        self.assertEqual(result, 16.0)

    def test_evaluate_expression_with_floats(self):
        self.calc.expression = "3.5+2.5"
        result = self.calc.evaluate_expression()
        self.assertEqual(result, 6.0)

if __name__ == "__main__":
    unittest.main()