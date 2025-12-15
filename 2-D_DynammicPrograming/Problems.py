# These problems are the part of Two Dimensional DP

def findTargetSumWays(self, nums, target: int) -> int:
    ways = self.recurse(nums, target, 0, 0)
    return ways

def recurse(self, nums, target, curr, idx):
    if idx == len(nums):
        return target == curr

    sub = self.recurse(nums, target, curr - nums[idx], idx + 1)
    add = self.recurse(nums, target, curr + nums[idx], idx + 1)

    return sub + add

# Memoized:
def findTargetSumWays(self, nums, target: int) -> int:
    memo = {}
    ways = self.recurse(memo, nums, target, 0, 0)
    return ways

def recurse(self, memo, nums, target, curr, idx):
    if idx == len(nums):
        return 1 if target == curr else 0
    if (idx, curr) in memo:
        return memo[(idx, curr)]

    sub = self.recurse(memo, nums, target, curr - nums[idx], idx + 1)
    add = self.recurse(memo, nums, target, curr + nums[idx], idx + 1)
    ways = sub + add
    memo[(idx, curr)] = ways

    return memo[(idx, curr)]

def uniquePaths(self, m: int, n: int) -> int:
    paths = self.recurse(m, n)
    return paths

def recurse(self, m, n):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1

    right = self.recurse(m, n - 1)
    down = self.recurse(m - 1, n)

    return right + down

def uniquePaths(self, m: int, n: int) -> int:
    memo = {}
    paths = self.recurse(memo, m, n)
    return paths

def recurse(self, memo, m, n):
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1

    right = self.recurse(memo, m, n - 1)
    down = self.recurse(memo, m - 1, n)
    memo[(m, n)] = right + down
    return memo[(m, n)]

def change(self, amount: int, coins) -> int:
    coins.sort()
    combos = self.recurse(amount, coins, 0)
    return combos

def recurse(self, amount, coins, idx):
    if amount == 0:
        return 1
    if amount < 0 or idx >= len(coins):
        return 0

    # Add the coin or skip the coin
    skip = self.recurse(amount, coins, idx + 1)
    add = self.recurse(amount - coins[idx], coins, idx)
    return add + skip

def change(self, amount: int, coins) -> int:
    coins.sort()
    memo = {}
    combos = self.recurse(memo, amount, coins, 0)
    return combos

def recurse(self, memo, amount, coins, idx):
    if (idx, amount) in memo:
        return memo[(idx, amount)]
    if amount == 0:
        return 1
    if amount < 0 or idx >= len(coins):
        return 0

    # Add the coin or skip the coin
    skip = self.recurse(memo, amount, coins, idx + 1)
    add = self.recurse(memo, amount - coins[idx], coins, idx)
    memo[(idx, amount)] = add + skip
    return memo[(idx, amount)]

def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    longest = self.recurse(0, 0, text1, text2)
    return longest

def recurse(self, i, j, t1, t2):
    if i == len(t1) or j == len(t2):
        return 0
    if t1[i] == t2[j]:
        return self.recurse(i + 1, j + 1, t1, t2) + 1

    curr = self.recurse(i, j + 1, t1, t2)
    next = self.recurse(i + 1, j, t1, t2)

    return max(curr, next)

def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    memo = {}
    longest = self.recurse(0, 0, text1, text2, memo)
    return longest

def recurse(self, i, j, t1, t2, memo):
    if (i, j) in memo:
        return memo[(i, j)]
    if i == len(t1) or j == len(t2):
        return 0
    if t1[i] == t2[j]:
        return self.recurse(i + 1, j + 1, t1, t2, memo) + 1

    curr = self.recurse(i, j + 1, t1, t2, memo)
    next = self.recurse(i + 1, j, t1, t2, memo)
    memo[(i, j)] = max(curr, next)
    return memo[(i, j)]

def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    dp = [[0 for j in range(len(text2) + 1)]
          for i in range(len(text1) + 1)]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[0][0]


def maxProfit(self, prices: List[int]) -> int:
    max_profit = self.recurse(prices, 0, False)
    return max_profit


def recurse(self, prices, idx, bought):
    if idx >= len(prices):
        return 0

    buy = 0
    sell = 0
    if bought:
        sell = prices[idx] + self.recurse(prices, idx + 2, not bought)
        skip = self.recurse(prices, idx + 1, bought)
        sell = max(skip, sell)
    else:
        buy = self.recurse(prices, idx + 1, not bought) - prices[idx]
        skip = self.recurse(prices, idx + 1, bought)
        buy = max(skip, buy)

    return max(buy, sell)


def maxProfit(self, prices: List[int]) -> int:
    memo = {}
    max_profit = self.recurse(prices, 0, False, memo)
    return max_profit


def recurse(self, prices, idx, bought, memo):
    if (idx, bought) in memo:
        return memo[(idx, bought)]
    if idx >= len(prices):
        return 0

    buy = 0
    sell = 0
    if bought:
        sell = prices[idx] + self.recurse(prices, idx + 2, not bought, memo)
        skip = self.recurse(prices, idx + 1, bought, memo)
        sell = max(skip, sell)
    else:
        buy = self.recurse(prices, idx + 1, not bought, memo) - prices[idx]
        skip = self.recurse(prices, idx + 1, bought, memo)
        buy = max(skip, buy)

    memo[(idx, bought)] = max(buy, sell)
    return memo[(idx, bought)]