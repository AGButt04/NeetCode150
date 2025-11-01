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

def robInCircle(self, nums):
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

def longestPalindrome(self, s):
    n = len(s)
    if n == 1:
        return s

    start = 0
    length = 0

    for i in range(n):
        # odd length
        left = i
        right = i

        while left >= 0 and right < n and s[left] == s[right]:
            if (right - left + 1) > length:
                start = left
                length = right - left + 1
            left -= 1
            right += 1

        # even length
        left = i
        right = i + 1

        while left >= 0 and right < n and s[left] == s[right]:
            if (right - left + 1) > length:
                start = left
                length = right - left + 1
            left -= 1
            right += 1

    return s[start: start + length]

def countSubstrings(self, s: str) -> int:
    n = len(s)
    pal_substrings = 0

    for i in range(n):
        # Odd length:
        left, right = i, i
        while left >= 0 and right < n and s[left] == s[right]:
            pal_substrings += 1
            left -= 1
            right += 1

        # Even length:
        left, right = i, i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            pal_substrings += 1
            left -= 1
            right += 1

    return pal_substrings

def countSubstrings_DP(self, s):
    n = len(s)
    pal_substrings = 0
    dp = [[False] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                pal_substrings += 1

    return pal_substrings