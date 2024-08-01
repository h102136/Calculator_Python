
import unittest
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculator.calculator import Calculator
from calculator.calculator import InputHandler

class TestInputHandler(unittest.TestCase):

    def setUp(self):
        self.input_handler = InputHandler()

    # patch the input() function to return a specific value
    @patch('builtins.input', side_effect=['(7+8.5)*5-9/3', 'Q'])
    # test the get_expression() method with a valid expression
    def test_get_expression_valid(self, mock_input):
        expression = self.input_handler.get_expression()
        self.assertEqual(expression, '(7+8.5)*5-9/3')

    @patch('builtins.input', side_effect=['invalid_expression', '(7+8.5)*5-9/3', 'Q'])
    # test the get_expression() method with an invalid expression followed by a valid expression
    def test_get_expression_invalid_then_valid(self, mock_input):
        expression = self.input_handler.get_expression()
        self.assertEqual(expression, '(7+8.5)*5-9/3')

    # test the validate_expression() method with a valid expression
    def test_validate_expression_valid(self):
        self.assertTrue(self.input_handler.validate_expression('(7+8.5)*5-9/3'))

    # test the validate_expression() method with an invalid expression
    def test_validate_expression_invalid_chars(self):
        self.assertFalse(self.input_handler.validate_expression('7+8.5a*5-9/3'))

    # test the validate_expression() method with consecutive operators
    def test_validate_expression_consecutive_operators(self):
        self.assertFalse(self.input_handler.validate_expression('7++8.5*5-9/3'))

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    # test the parse_expression() method with a simple expression
    def test_evaluate_expression_simple(self):
        result = self.calculator.evaluate_expression('2+3')
        self.assertEqual(result, 5)

    # test the parse_expression() method with a complex expression
    def test_evaluate_expression_complex(self):
        result = self.calculator.evaluate_expression('(7+8.5)*5-9/3')
        self.assertAlmostEqual(result, 74.5)
    
    # test the parse_expression() method with a float result
    def test_evaluate_expression_with_floats(self):
        result = self.calculator.evaluate_expression('7.5*2')
        self.assertAlmostEqual(result, 15.0)

    # test the parse_expression() method with parentheses
    def test_evaluate_expression_with_parentheses(self):
        result = self.calculator.evaluate_expression('2*(3+4)')
        self.assertEqual(result, 14)

if __name__ == '__main__':
    unittest.main()
