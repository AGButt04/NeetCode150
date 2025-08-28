# This file has all the problems in the Arrays & Hashing
# section of the NeetCode150 with the explanations.

# Problem-1:
def hasDuplicate(nums):
    duplicates = {}

    for n in nums:
        if n in duplicates:
            return True

        duplicates[n] = duplicates.get(n, 0) + 1

    return False