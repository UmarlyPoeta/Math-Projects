import unittest
from unittest.mock import patch
from io import StringIO

# Import the function to be tested
from egyptian_multiplication import egyptian_multiplication

class TestEgyptianMultiplication(unittest.TestCase):

    def test_egyptian_multiplication(self):
        # Test case 1
        self.assertEqual(egyptian_multiplication(7, 5), 35)

        # Test case 2
        self.assertEqual(egyptian_multiplication(12, 3), 36)

        # Test case 3
        self.assertEqual(egyptian_multiplication(20, 4), 80)


if __name__ == '__main__':
    unittest.main()
