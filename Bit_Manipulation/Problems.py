# This file has all the problems in the 1-D Dynamic Programming
# section of the NeetCode150 with the explanations.

def singleNumber(nums):
    nums.sort()
    single_number = -1
    index = 0

    while index < len(nums) - 1:
        if nums[index] == nums[index + 1]:
            index += 2
        else:
            return nums[index]

    return nums[index]

def hammingWeight(self, n: int) -> int:
    ones = 0

    while n:
        if n & 1 == 1:
            ones += 1
        n >>= 1

    return ones

if __name__ == '__main__':