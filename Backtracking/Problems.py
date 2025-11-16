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

if '__main__' == __name__:
    candidates = [9, 2, 2, 4, 6, 1, 5]
    target = 8
    # Output: [
    #     [1, 2, 5],
    #     [2, 2, 4],
    #     [2, 6]
    # ]
    combs = combinationSum(candidates, target)
    for comb in combs:
        print(comb)
