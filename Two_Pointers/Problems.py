# This file has all the problems in the Two Pointers
# section of the NeetCode150 with the explanations.

import string

def isPalindrome(s):
    st = s.replace(' ', '')
    st = st.lower()
    translator = str.maketrans('', '', string.punctuation)
    st = st.translate(translator)
    left = 0
    right = len(st) - 1

    while left < right:
        char = st[left]
        ch = st[right]
        if char != ch:
            return False

        left += 1
        right -= 1

    return True

def twoSum(numbers, target):
    left = 0
    right = len(numbers)-1

    while left < right:
        num1 = numbers[left]
        num2 = numbers[right]
        current_sum = num1 + num2

        if current_sum == target:
            return [left+1, right+1]
        elif current_sum > target:
            right -= 1
        else:
            left += 1

    return None

def threeSum(nums):
    triples = []
    nums.sort()

    for i, num in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            curr_sum = num + nums[left] + nums[right]

            if curr_sum == 0:
                triples.append([num, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while right > left and nums[right] == nums[right + 1]:
                    right -= 1

            elif curr_sum > 0:
                right -= 1
            else:
                left += 1

    return triples

def maxArea(heights):
    maxA = 0
    left = 0
    right = len(heights) - 1

    while left < right:
        height = min(heights[left], heights[right])
        width = right - left
        currArea = height * width
        maxA = max(maxA, currArea)

        if heights[left] > heights[right]:
            right -= 1
        elif heights[left < heights[right]]:
            left += 1
        else:
            left += 1
            right -= 1

    return maxA

if __name__ == '__main__':
    s = "Was it a car or a cat I saw?"
    print(isPalindrome(s))