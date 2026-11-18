# Online Assessment Preparation and Review

def longestSubarray1(nums: list[int], k: int) -> int:
    length = len(nums)
    if length <= 0:
        return 0

    max_subarray = 0

    for i in range(length):
        curr_sum = 0
        for j in range(i, length):
            curr_sum += nums[j]

            if curr_sum == k:
                max_subarray = max(max_subarray, j - i + 1)

    return max_subarray

def longestSubarray(nums: list[int], k: int) -> int:
    # Efficient Version
    length = len(nums)
    if length <= 0:
        return 0

    prefix_sums = { 0 : -1 }
    pre_sum = 0
    max_subarray = 0
    for i in range(length):
        pre_sum += nums[i]

        if pre_sum - k in prefix_sums:
            max_subarray = max(max_subarray, i - prefix_sums[pre_sum - k])
        if pre_sum not in prefix_sums:
            prefix_sums[pre_sum] = i

    return max_subarray



if __name__ == '__main__':
    # nums = [1, -1, 5, -2, 3]
    # k = 3
    nums = [3, 5, 7]
    k = 3
    print(longestSubarray(nums, k))