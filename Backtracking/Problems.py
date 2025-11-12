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
