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

def countBits(n: int):
    ones_array = [0] * (n + 1)

    for i in range(1, n + 1):
        num = i
        while num != 0:
            ones_array[i] += 1
            num = num & (num - 1)

    return ones_array

def missingNumber(self, nums):
    n = len(nums)
    r_sum = n
    c_sum = 0

    for i, n in enumerate(nums):
        r_sum += i
        c_sum += n

    return r_sum - c_sum

if __name__ == '__main__':
    print(2 & 1)