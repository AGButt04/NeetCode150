# This file has all the problems in the Two Pointers
# section of the NeetCode150 with the explanations.

def search(nums, target):
    left = 0
    right = len(nums) - 1

    for i in range(len(nums)):
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # Time Complexity: O(log n) because at each step we are removing
    # half of the problem. It's a classic binary search
    # Space Complexity: O(1) we are just storing two pointers.
    return -1

def searchMatrix(matrix, target):
    n = len(matrix[0])

    for r, row in enumerate(matrix):
        left = 0
        right = n - 1

        while left <= right:
            c = (left + right) // 2
            num = matrix[r][c]

            if num == target:
                return True
            elif num > target:
                right = c - 1
            else:
                left = c + 1

    # Time complexity: O(m * log n) as we perform binary search on
    # each row with n numbers, and there are m rows in the matrix
    # Space complexity: O(1) Space complexity for just pointers.
    return False