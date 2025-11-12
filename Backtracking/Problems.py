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

def generateParenthesis(self, n: int) -> List[str]:
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