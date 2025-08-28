# This file has all the problems in the Arrays & Hashing
# section of the NeetCode150 with the explanations.

# Problem-1 (Contains Duplicate):
def hasDuplicate(nums):
    duplicates = {}

    for n in nums:
        if n in duplicates:
            return True

        duplicates[n] = duplicates.get(n, 0) + 1

    return False

# Problem-2 (Is Anagram):
def isAnagram(s, t):
    freq_1 = {}
    freq_2 = {}

    for c in s:
        freq_1[c] = freq_1.get(c, 0) + 1

    for c in t:
        freq_2[c] = freq_2.get(c, 0) + 1

    return freq_1 == freq_2

