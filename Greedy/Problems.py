# This file has all the problems in the Greedy
# section of the NeetCode150 with the explanations.
import math


# Function: maxSubArray
# Purpose: Find the maximum subarray sum (Kadane’s Algorithm)
def maxSubArray(nums):
    Sum = 0
    maxSum = -math.inf  # Initialize to the smallest possible value

    for i in range(len(nums)):
        Sum += nums[i]               # Add current number to running sum
        if Sum <= nums[i]:           # If current number is better alone
            Sum = nums[i]            # Start new subarray from here
        maxSum = max(maxSum, Sum)    # Update global max if needed

    # Time Complexity: O(n) — single pass through the array
    # Space Complexity: O(1) — uses only a few variables
    return maxSum


# Function: canJump
# Purpose: Check if you can reach the last index (Greedy approach)
def canJump(nums):
    length = len(nums)
    goal = length - 1                # Start with last index as target

    # Traverse backwards to see if current index can reach the goal
    for i in range(len(nums) - 2, -1, -1):
        check = nums[i] + i          # Farthest reachable index from i
        if check >= goal:            # If we can reach or go beyond goal
            goal = i                 # Move goal to current position

    # Time Complexity: O(n) — single backward pass
    # Space Complexity: O(1) — constant extra space
    return goal == 0

def jump(self, nums) -> int:
    jumps = 0
    left = right = 0

    while right < len(nums) - 1:
        farthest = 0
        for idx in range(left, right + 1):
            farthest = max(farthest, idx + nums[idx])

        left = right + 1
        right = farthest
        jumps += 1

    return jumps
