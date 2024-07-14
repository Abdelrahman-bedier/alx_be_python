import unittest
from simple_calculator import SimpleCalculator 


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertIsNone(self.calc.divide(10, 0))
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.