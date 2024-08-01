
import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculator.calculator_python import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # test case for user input
    @patch('builtins.input', side_effect=['2+3*5', 'Q'])
    def test_get_expression_valid(self, mock_input):
        expression = self.calculator.get_expression()
        self.assertEqual(expression, '2+3*5')

    @patch('builtins.input', side_effect=['2++3', 'Q'])
    def test_get_expression_invalid(self, mock_input):
        with self.assertRaises(SystemExit):
            self.calculator.get_expression()

    # test case for expression validation
    def test_validate_expression(self):
        self.calculator.expression = "2+3*5"
        self.assertTrue(self.calculator.validate_expression())
        self.calculator.expression = "2+3*5a"
        self.assertFalse(self.calculator.validate_expression())
        self.calculator.expression = "(2+3)*5"
        self.assertTrue(self.calculator.validate_expression())
        self.calculator.expression = "2++3"
        self.assertFalse(self.calculator.validate_expression())

    def test_evaluate_expression(self):
        self.calculator.expression = "2+3*5"
        self.assertEqual(self.calculator.evaluate_expression(), 17)
        self.calculator.expression = "(2+3)*5"
        self.assertEqual(self.calculator.evaluate_expression(), 25)
        self.calculator.expression = "10/2.5+3*4"
        self.assertEqual(self.calculator.evaluate_expression(), 16)
        self.calculator.expression = "10/(5-3)"
        self.assertEqual(self.calculator.evaluate_expression(), 5)

    def test_reinitialize(self):
        self.calculator.expression = "2++3"
        self.assertFalse(self.calculator.validate_expression())
        
        with patch('builtins.input', side_effect=['2+3*5']):
            self.calculator.reinitialize()
        
        self.calculator.expression = "2+3*5"
        self.assertTrue(self.calculator.validate_expression())

    @patch('builtins.input', side_effect=['2+3*5', 'Q'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_valid_expression(self, mock_stdout, mock_input):
        calc = Calculator()
        calc.get_expression()
        if not calc.validate_expression():
            calc.reinitialize()
        else:
            result = calc.evaluate_expression()
            print(f"The result of the expression is: {result}")
        
        self.assertIn("The result of the expression is: 17", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
