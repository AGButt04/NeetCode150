# This file has all the problems in the Two Pointers
# section of the NeetCode150 with the explanations.

def search(nums, target):
    left = 0
    right = len(nums) - 1

    # Should be while left <= right, not for loop
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # Time Complexity: O(log n) - halve search space each iteration
    # Space Complexity: O(1) - only using pointers
    return -1


def searchMatrix(matrix, target):
    # This works but can be optimized - treat 2D matrix as 1D array
    # Current approach: O(m * log n) - binary search each row

    for row in matrix:
        left = 0
        right = len(row) - 1

        while left <= right:
            mid = (left + right) // 2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

    return False


def searchMatrixOptimal(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        # Convert 1D index back to 2D coordinates
        row, col = mid // n, mid % n
        val = matrix[row][col]

        if val == target:
            return True
        elif val > target:
            right = mid - 1
        else:
            left = mid + 1

    # Alternative O(log(m*n)) solution - treat matrix as flattened array
    return False