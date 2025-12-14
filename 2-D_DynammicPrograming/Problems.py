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