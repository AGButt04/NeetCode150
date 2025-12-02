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

def isHappy(self, n):
    visited = set()

    while n not in visited:
        visited.add(n)
        if n == 1:
            return True

        new_n = 0
        while n:
            dig = n % 10
            n = n // 10
            new_n += dig ** 2

        n = new_n

    return False

def plusOne(self, digits):
    carry = 1
    idx = 0
    digits.reverse()

    while carry == 1 and idx < len(digits):
        add = digits[idx] + carry
        carry = add // 10
        add = add % 10

        digits[idx] = add
        idx += 1

    if carry == 1:
        digits.append(1)

    digits.reverse()
    return digits

def spiralOrder(self, matrix):
    order = []
    m, n = len(matrix), len(matrix[0])
    left, right = 0, n
    top, bottom = 0, m

    while left < right and top < bottom:
        # Go right
        for r in range(left, right):
            order.append(matrix[top][r])
        top += 1

        # Go Down
        for d in range(top, bottom):
            order.append(matrix[d][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break

        # Go left
        for l in range(right - 1, left - 1, -1):
            order.append(matrix[bottom - 1][l])
        bottom -= 1

        # Go up
        for u in range(bottom - 1, top - 1, -1):
            order.append(matrix[u][left])
        left += 1

    return order