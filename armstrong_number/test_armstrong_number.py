import unittest
from armstrong_number import is_armstrong_number

class TestIsArmstrongNumber(unittest.TestCase):

    def test_positive_armstrong_number(self):
        result = is_armstrong_number(153)
        self.assertTrue(result)

    def test_negative_armstrong_number(self):
        result = is_armstrong_number(-371)
        self.assertTrue(result)

    def test_zero_armstrong_number(self):
        result = is_armstrong_number(0)
        self.assertTrue(result)

    def test_positive_non_armstrong_number(self):
        result = is_armstrong_number(123)
        self.assertFalse(result)

    def test_negative_non_armstrong_number(self):
        result = is_armstrong_number(-1634)
        self.assertFalse(result)

    def test_single_digit_armstrong_number(self):
        result = is_armstrong_number(9)
        self.assertTrue(result)

    def test_large_armstrong_number(self):
        result = is_armstrong_number(9474)
        self.assertTrue(result)

    def test_large_non_armstrong_number(self):
        result = is_armstrong_number(9475)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
