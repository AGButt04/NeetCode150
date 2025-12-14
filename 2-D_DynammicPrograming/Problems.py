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