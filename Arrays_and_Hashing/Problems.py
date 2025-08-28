# This file has all the problems in the Arrays & Hashing
# section of the NeetCode150 with the explanations.

from collections import defaultdict
import heapq

# Problem-1 (Contains Duplicate):
def hasDuplicate(nums):
    # In this problem, we are trying to find if the given array
    # has a duplicate or not, return True or False based on that.
    duplicates = {}
    # For that, we will use a dictionary to keep track of each
    # number into the array, and if the same number appears again
    # we know that this array does contain a duplicate.

    for n in nums:
        # Duplicate check
        if n in duplicates:
            return True
        # Put each number into the dictionary and keep the count (not important here)
        duplicates[n] = duplicates.get(n, 0) + 1

    # Return false at the end if no duplicate found
    # Time complexity: O(n) => As it walks through the array once
    # Space complexity: O(n) => As we are creating a dictionary side by side
    return False

# Problem-2 (Is Anagram):
def isAnagram(s, t):
    # Here we are checking if two string are anagrams of each other or not
    # Anagrams means same characters but in different order with same frequency.
    freq_1 = {}
    freq_2 = {}
    # For that, we can use two dictionaries where we will populate those dictionaries
    # with both strings and at the end we will check if they are equal or not, as they
    # should have all the same characters with the exact same count of each character.

    for c in s:
        # Populate Dict 1
        freq_1[c] = freq_1.get(c, 0) + 1

    for c in t:
        # Populate Dict 2
        freq_2[c] = freq_2.get(c, 0) + 1

    # This returns the appropriate value
    # Time complexity: O(n) (Dict1 Traversal) + O(n) (Dict2 Traversal) => O(n)
    # Space complexity: O(n) (Dict1 Storage) + O(n) (Dict2 Storage) => O(n)
    return freq_1 == freq_2

# Problem-3 (Two Sum)
def twoSum(nums, target):
    # In this problem, we are trying to find the two numbers whose sum adds upto
    # the target integer given, and return their indexes as a list at the end.

    indexes = {}
    # For that, we can use a dictionary to keep track of the indexes of each
    # number in the array. This could be done easy enough if we could sort the
    # array with two pointers, but that increases the runtime O(n log n) time.


    for i in range(len(nums)):
        # We will iterate over all the number and at each index, we will
        # subtract current number from target and get the remaining value.
        check = target - nums[i]

        if check in indexes:
            # If that value is in indexes dictionary that means this target
            # can be formed, so we will just return the index of the remaining
            # value retrieved from indexes dictionary and current index (i).
            return [indexes[check], i]

        indexes[nums[i]] = i # Put each number in dictionary with its index as value

    # Return None if no combo adds upto target
    # Time complexity: O(n) => As it walks through the array once
    # Space complexity: O(n) => As we are creating a dictionary side by side
    return None

# Problem-4 (Group Anagrams)
def groupAnagrams(strs):
    frequencies = []  # list of frequency dicts for each string
    groupings = []  # final list of grouped anagrams
    grouped = [False] * len(strs)  # marks whether a string has already been grouped

    # Step 1: Build frequency map for each string
    for st in strs:
        curr_dict = {}
        for char in st:
            curr_dict[char] = curr_dict.get(char, 0) + 1
        frequencies.append(curr_dict)

    # Step 2: Compare frequency maps to form groups
    for i, st in enumerate(strs):
        if grouped[i]:  # skip if this string is already grouped
            continue

        curr_list = [st]  # start a new group with current string
        grouped[i] = True  # mark as grouped

        # Compare with all later strings
        for j in range(i + 1, len(strs)):
            if frequencies[j] == frequencies[i] and not grouped[j]:
                curr_list.append(strs[j])
                grouped[j] = True  # mark as grouped

        groupings.append(curr_list)  # add the completed group

    return groupings


# Problem-4 (Group Anagrams simpler + standard approach)
def groupAnagramsII(strs):
    groups = defaultdict(list)  # key: sorted string, value: list of words

    # Step 1: Sort characters of each string
    for st in strs:
        string = sorted(st)  # e.g. "eat" -> ['a','e','t']
        key = "".join(string)  # join -> "aet"
        groups[key].append(st)  # group words by key

    # Step 2: Return all groups
    return list(groups.values())

# Problem-5 (Top k frequent Elements)
def topKFrequent(nums, k):
    # In this problem, we are trying to find the top k frequent element
    # from the array, means k most occurring elements. For that we will
    # use a dictionary which will keep track of the frequencies of all
    # the numbers, and a minheap which will sort the number based on their frequencies.
    frequencies = {}
    heap = []
    k_freq = []

    for n in nums:
        # Populate the Map with the frequencies
        frequencies[n] = frequencies.get(n, 0) + 1

    for key, value in frequencies.items():
        # Then we will walk over all the elements in the dictionary and
        # push the tuples (value (Frequency), key (Number)) onto the heap.
        # The order is (freq, number) because then the heap will sort based
        # on the first element of the tuple so value has to be first.
        heapq.heappush(heap, (value, key))
        if len(heap) > k:
            # If the heap has more than k elements then we remove the top,
            # as our concern is just the top k elements, so size should be k.
            heapq.heappop(heap)

    # Then we iterate over the heap that has k elements and just
    # add those elements (numbers) into the list required for return.
    for freq, num in heap:
        k_freq.append(num)

    # Time complexity: O(n) => Populate Dictionary + O(n log n) (Populate heap)
    # + O(k) (Populating the list) =>> O(n + n log n + k) => O(n log n)
    # Space complexity: O(n) (Dictionary) + O(n) (Heap) + O(k) (List) => O(n + k)

    return k_freq


if __name__ == '__main__':
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    print(groupAnagramsII(strs))