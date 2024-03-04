import unittest
from det_matrix.det_matrix import determinant

class TestMatrixDeterminant(unittest.TestCase):

    def test_1x1_matrix(self):
        matrix = [[5]]
        self.assertEqual(determinant(matrix), 5)

    def test_2x2_matrix(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        self.assertEqual(determinant(matrix), -2)

    def test_3x3_matrix(self):
        matrix = [
            [2, 0, 1],
            [0, 1, 0],
            [1, 2, 3]
        ]
        self.assertEqual(determinant(matrix), 3)

    def test_4x4_matrix(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        self.assertEqual(determinant(matrix), 0)

    def test_5x5_matrix(self):
        matrix = [
            [1, 0, 0, 0, 0],
            [0, 2, 0, 0, 0],
            [0, 0, 3, 0, 0],
            [0, 0, 0, 4, 0],
            [0, 0, 0, 0, 5]
        ]
        self.assertEqual(determinant(matrix), 120)

    def test_non_square_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        with self.assertRaises(ValueError):
            determinant(matrix)

if __name__ == '__main__':
    unittest.main()
