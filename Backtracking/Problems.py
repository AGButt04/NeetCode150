# This file has all the problems in the Backtracking
# section of the NeetCode150 with the explanations.

def subsets(nums):
    subsets = []
    sets = []

    def recurse(index):
        if index >= len(nums):
            subsets.append(sets.copy())
            return

        sets.append(nums[index])
        recurse(index + 1)
        sets.pop()
        recurse(index + 1)

    recurse(0)
    return subsets

def generateParenthesis(self, n: int):
    parenthesis = []

    def recurse(string, open_count, close_count):
        if open_count < close_count or open_count > n:
            return
        if len(string) == n * 2:
            parenthesis.append(string)
            return

        recurse(string + "(", open_count + 1, close_count)
        recurse(string + ")", open_count, close_count + 1)

    recurse("", 0, 0)

    return parenthesis

def combinationSum(nums, target):
    combinations = []

    def recurse(combo, num):
        if num == 0:
            com = combo.copy()
            com.sort()
            if com not in combinations:
                combinations.append(com)
            return
        if num < 0:
            return

        for n in nums:
            combo.append(n)
            num -= n
            recurse(combo, num)
            combo.pop()
            num += n

    recurse([], target)
    return combinations

def combinationSum2(candidates, target):
    combinations = []
    candidates.sort()

    def recurse(idx, curr, comb):
        if curr == target:
            combinations.append(comb.copy())
            return
        if curr > target or idx >= len(candidates):
            return

        # Add this number to the combination
        comb.append(candidates[idx])
        recurse(idx + 1, curr + candidates[idx], comb)
        comb.pop()

        # Skip the duplicates
        while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
            idx += 1

        # Don't add this number to the combination
        recurse(idx + 1, curr, comb)

    recurse(0, 0, [])
    return combinations

def permute(self, nums):
    self.permutations = []
    self.backtrack([], nums, [False] * len(nums))
    return self.permutations

def backtrack(self, perm, nums, pick):
    if len(perm) == len(nums):
        self.permutations.append(perm.copy())
        return

    for i in range(len(nums)):
        if not pick[i]:
            perm.append(nums[i])
            pick[i] = True
            self.backtrack(perm, nums, pick)
            perm.pop()
            pick[i] = False

def subsetsWithDup(self, nums):
    subsets = []
    nums.sort()

    def backtrack(idx, curr_set):
        if idx == len(nums):
            subsets.append(curr_set.copy())
            return

        curr_set.append(nums[idx])
        backtrack(idx + 1, curr_set)
        curr_set.pop()

        while idx + 1 < len(nums) and nums[idx + 1] == nums[idx]:
            idx += 1

        backtrack(idx + 1, curr_set)

    backtrack(0, [])
    return subsets

def exist(self, board: List[List[str]], word: str) -> bool:
    m = len(board)
    n = len(board[0])
    visited = set()

    def backtrack(r, c, idx):
        if idx == len(word):
            return True

        if (r < 0 or r >= m) or (c < 0 or c >= n):
            return False

        if word[idx] != board[r][c] or (r, c) in visited:
            return False

        visited.add((r, c))
        up = backtrack(r - 1, c, idx + 1)
        down = backtrack(r + 1, c, idx + 1)
        left = backtrack(r, c - 1, idx + 1)
        right = backtrack(r, c + 1, idx + 1)

        res = up or down or left or right
        visited.remove((r, c))

        return res

    for i in range(m):
        for j in range(n):
            if backtrack(i, j, 0):
                return True

    return False


if '__main__' == __name__:
    candidates = [9, 2, 2, 4, 6, 1, 5]
    target = 8
    # Output: [
    #     [1, 2, 5],
    #     [2, 2, 4],
    #     [2, 6]
    # ]
    combs = combinationSum2(candidates, target)
    for comb in combs:
        print(comb)
