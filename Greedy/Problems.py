# This file has all the problems in the Greedy
# section of the NeetCode150 with the explanations.
import math

def maxSubArray(nums):
    Sum = 0
    maxSum = -math.inf

    for i in range(len(nums)):
        Sum += nums[i]
        if Sum <= nums[i]:
            Sum = nums[i]

        maxSum = max(maxSum, Sum)

    # Time complexity: O(n) for going through the array once
    # Space complexity: O(1) for keeping track of just 2 variables
    return maxSum