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

# Problem-3 (Two Sum)
def twoSum(nums, target):
    indexes = {}

    for i in range(len(nums)):
        check = target - nums[i]

        if check in indexes:
            return [indexes[check], i]

        indexes[nums[i]] = i

    return None

# Problem-3 (Group Anagrams)
def groupAnagrams(strs):
    frequencies = []
    groupings = []
    grouped = [False] * len(strs)

    for st in strs:
        curr_dict = {}
        for char in st:
            curr_dict[char] = curr_dict.get(char, 0) + 1

        frequencies.append(curr_dict)

    for i, st in enumerate(strs):
        if grouped[i]:
            continue

        curr_list = [st]
        grouped[i] = True
        for j in range(i + 1, len(strs)):
            if frequencies[j] == frequencies[i] and not grouped[j]:
                curr_list.append(strs[j])
                grouped[j] = True

        groupings.append(curr_list)

    return groupings

if __name__ == '__main__':
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    print(groupAnagrams(strs))