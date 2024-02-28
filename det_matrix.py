

def minor(matrix, row, col):
    return [row[:col] + row[col+1:] for row in (matrix[:row] + matrix[row+1:])]


def determinant(matrix):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]

    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(len(matrix[0])):
        det += ((-1) ** col) * matrix[0][col] * determinant(minor(matrix, 0, col))

    return det
