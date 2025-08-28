# This file has all the problems in the Arrays & Hashing
# section of the NeetCode150 with the explanations.

from collections import defaultdict
import heapq

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

# Problem-4 (Group Anagrams)
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

# Problem-4 (Group Anagrams Simpler Approach)
def groupAnagramsII(strs):
    groups = defaultdict(list)

    for st in strs:
        string = sorted(st)
        key = "".join(string)
        groups[key].append(st)

    return list(groups.values())

# Problem-5 (Top k frequent Elements)
def topKFrequent(nums, k):
    frequencies = {}
    heap = []
    k_freq = []

    for n in nums:
        frequencies[n] = frequencies.get(n, 0) + 1

    for key, value in frequencies.items():
        heapq.heappush(heap, (value, key))
        if len(heap) > k:
            heapq.heappop(heap)

    for key, value in heap:
        k_freq.append(value)

    return k_freq


if __name__ == '__main__':
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    print(groupAnagramsII(strs))