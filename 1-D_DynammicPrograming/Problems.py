# This file has all the problems in the 1-D Dynamic Programming
# section of the NeetCode150 with the explanations.

def climbStairs(self, n):
    memo = {}

    def steps(memo, num):
        if num in memo:
            return memo[num]
        if num < 0:
            return 0
        if num == 0:
            return 1

        one_step = steps(memo, num - 1)
        two_step = steps(memo, num - 2)

        total = one_step + two_step
        memo[num] = total

        return total

    return steps(memo, n)

def minCostClimbingStairs(self, cost):
    memo = {}

    def stairs(index):
        if index in memo:
            return memo[index]
        if index >= len(cost):
            return 0

        total = cost[index] + min(stairs(index + 1), stairs(index + 2))

        memo[index] = total
        return total

    return min(stairs(0), stairs(1))

def rob(self, nums):
    memo = {}

    def recurse(index):
        if index in memo:
            return memo[index]
        if index >= len(nums):
            return 0

        rob_this = nums[index] + recurse(index + 2,)
        skip_this = recurse(index + 1)

        result = max(rob_this, skip_this)
        memo[index] = result

        return result

    return recurse(0)

def robInCircle(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    first = nums[:-1]
    second = nums[1:]

    first_res = self.robbing(first)
    second_res = self.robbing(second)

    return max(first_res, second_res)

def robbing(self, nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [-1] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        rob_this = nums[i] + dp[i - 2]
        skip_this = dp[i - 1]

        dp[i] = max(rob_this, skip_this)

    return dp[-1]

