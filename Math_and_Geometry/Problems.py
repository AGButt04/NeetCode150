# This file has all the problems in the Backtracking
# section of the NeetCode150 with the explanations.

def rotate(self, matrix) -> None:
    m = len(matrix)
    n = len(matrix[0])
    matrix.reverse()

    for i in range(m):
        for j in range(i + 1, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

def setZeroes(self, matrix) -> None:
    m = len(matrix)
    n = len(matrix[0])
    stack = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                stack.append((i, j))

    while stack:
        row, col = stack.pop()
        # Up
        for i in range(row - 1, -1, -1):
            matrix[i][col] = 0
            # Down
        for i in range(row + 1, m, 1):
            matrix[i][col] = 0
        # Left
        for i in range(col - 1, -1, -1):
            matrix[row][i] = 0
        # Right
        for i in range(col + 1, n, 1):
            matrix[row][i] = 0