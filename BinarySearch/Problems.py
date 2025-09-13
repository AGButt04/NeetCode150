# This file has all the problems in the Two Pointers
# section of the NeetCode150 with the explanations.
import math

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

def minEatingSpeed(piles, h):
    left = 1  # The smallest possible eating speed
    right = max(piles)  # The largest possible eating speed (eat biggest pile in 1 hour)
    upperBound = right  # Initialize answer with worst-case speed

    while left <= right:  # Standard binary search loop
        mid = (left + right) // 2  # Candidate eating speed

        count = 0  # Total hours needed at speed = mid
        for p in piles:
            count += math.ceil(float(p) / mid)
            # divide each pile size by speed, round up (since partial piles take full hour)

        if count <= h:  # If we can finish within h hours
            upperBound = mid  # This speed works, try slower speed to minimize
            right = mid - 1  # Search left half
        else:
            left = mid + 1  # Too slow, must increase speed

    # Time complexity: O(n * log n) => O(log n) for BS, and O(n) for going over the piles each time
    # Space Complexity: O(1) as we are just keeping track of three variables.
    return upperBound


class TimeMap:
    def __init__(self):
        # Dictionary where:
        # key -> list of (timestamp, value) pairs (sorted by timestamp in order of insertion)
        self.timestamps = {}
        # Space Complexity: O(n), since every call to set() stores one new (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key is new, initialize with a list
        if key not in self.timestamps:
            self.timestamps[key] = [(timestamp, value)]
            return

        # Otherwise, append new (timestamp, value) to the list
        self.timestamps[key].append((timestamp, value))
        # Time Complexity: O(1), dictionary lookup + list append

    def get(self, key: str, timestamp: int) -> str:
        # If key doesn’t exist, return empty string
        if key not in self.timestamps:
            return ""

        pairs = self.timestamps[key]  # list of (timestamp, value)
        left = 0
        right = len(pairs) - 1
        mostRecent = -1  # stores index of latest timestamp <= query timestamp

        # Binary search for the greatest timestamp <= given timestamp
        while left <= right:
            mid = (left + right) // 2
            time, value = pairs[mid]

            if time <= timestamp:
                mostRecent = mid       # candidate found
                left = mid + 1         # search to the right for newer candidate
            else:
                right = mid - 1        # too new, search left

        # If found, return value; otherwise, return ""
        # Time Complexity: O(log n) due to binary search
        return pairs[mostRecent][1] if mostRecent >= 0 else ""



