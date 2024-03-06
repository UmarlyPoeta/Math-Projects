import unittest

def peasant_multiplication(num1, num2, s=0):
    if num1 % 2 != 0:
        s += num2
    if num1 == 1:
        return s
    return peasant_multiplication(num1 // 2, num2 * 2, s)

class TestPeasantMultiplication(unittest.TestCase):

    def test_multiplication_with_odd_num1(self):
        result = peasant_multiplication(5, 3)
        self.assertEqual(result, 15)

    def test_multiplication_with_even_num1(self):
        result = peasant_multiplication(6, 4)
        self.assertEqual(result, 24)

    def test_multiplication_with_num1_equals_1(self):
        result = peasant_multiplication(1, 8)
        self.assertEqual(result, 8)

    def test_multiplication_with_zero_as_num1(self):
        result = peasant_multiplication(1, 20)
        self.assertEqual(result, 20)

    def test_multiplication_with_negative_num1(self):
        result = peasant_multiplication(3, 5)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()
