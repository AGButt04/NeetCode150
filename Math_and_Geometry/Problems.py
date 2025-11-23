# This file has all the problems in the Backtracking
# section of the NeetCode150 with the explanations.

def rotate(self, matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])
    matrix.reverse()

    for i in range(m):
        for j in range(i + 1, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
