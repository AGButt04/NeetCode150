# This file has all the problems in the 1-D Dynamic Programming
# section of the NeetCode150 with the explanations.

import math

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

def coinChange(self, coins, amount):
    memo = {}

    def recurse(target):
        if target in memo:
            return memo[target]
        if target == 0:
            return 0

        min_coins = math.inf
        for coin in coins:
            if target - coin >= 0:
                curr_coins = recurse(target - coin) + 1
                min_coins = min(min_coins, curr_coins)

        memo[target] = min_coins
        return min_coins

    min_coins = recurse(amount)
    return -1 if min_coins == math.inf else min_coins

def coinChange(self, coins, amount):
    dp = [math.inf] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[amount] == math.inf else dp[amount]

def maxProduct(self, nums) -> int:
    curr_min = curr_max = result = nums[0]

    for n in nums[1:]:
        if n < 0:
            curr_min, curr_max = curr_max, curr_min

        curr_min = min(n, n * curr_min)
        curr_max = max(n, n * curr_max)

        result = max(result, curr_max)

    return result

def wordBreak(s, wordDict):
    length = len(s)
    breaks = [False] * (length + 1)
    breaks[0] = True

    for i in range(length + 1):
        for j in range(i + 1):
            if breaks[j] and s[j : i] in wordDict:
                breaks[i] = True

    print(breaks)
    return breaks[length]


def lengthOfLIS(nums):
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 1, - 1, -1):
        for j in range(i - 1, -2, -1):
            LIS = dp[i + 1][j + 1]

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, dp[i + 1][i + 1] + 1)

            dp[i][j + 1] = LIS

    return dp

def numDecodings(self, s: str) -> int:
    if s[0] == '0':
        return 0

    decodings = [0] * len(s);
    decodings[0] = 1 if s[0] != '0' else 0

    for i in range(1, len(s)):
        char = s[i]

        if char != '0':
            decodings[i] = decodings[i - 1]

        num = int(s[i - 1: i + 1])
        if 10 <= num <= 26:
            if i - 2 >= 0:
                decodings[i] += decodings[i - 2]
            else:
                decodings[i] += 1

    return decodings[-1]

def lengthOfLIS(self, nums):
    n = len(nums)
    max_seq = 0
    dp = [1] * n

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

        max_seq = max(max_seq, dp[i])

    return max_seq


if __name__ == '__main__':
    nums = [9, 1, 4, 2, 3, 3, 7]
    dp = lengthOfLIS(nums)

    for row in dp:
        print(row)
