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

    # Alternative O(log(m * n)) solution - treat matrix as flattened array
    return False

def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        curr = nums[mid]

        if curr > nums[right]:
            left = mid + 1
        else:
            right = mid

    # Time complexity: O(log n) for doing binary search
    # Space complexity: O(1) for just keeping track of pointers
    return min(nums[0], nums[left])

def searchRotated(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (right + left) // 2  # Standard binary search mid index

        if nums[mid] == target:  # Found the target
            return mid

        # Case 1: Left half is sorted
        if nums[left] <= nums[mid]:
            # Check if target is inside the sorted left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Search in left half
            else:
                left = mid + 1  # Search in right half

        # Case 2: Right half is sorted
        else:
            # Check if target is inside the sorted right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1  # Search in right half
            else:
                right = mid - 1  # Search in left half

    # Time complexity: O(log n) for doing binary search
    # Space complexity: O(1) for just keeping track of pointers
    return -1