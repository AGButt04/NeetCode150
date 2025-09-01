# This file has all the problems in the Two Pointers
# section of the NeetCode150 with the explanations.

import string

# Problem-1:
def isPalindrome(s):
    # In this problem, we are just checking if a given string is a palindrome or not
    # For that, we will use two pointers approach, where we will start both pointers
    # from both ends of the string and walk them towards each other char by char.

    st = s.replace(' ', '') # Getting rid of all the whitespaces
    st = st.lower()         # Lower casing the whole string for convenience
    # This is the important where we are replacing all the punctuations
    # with the empty string so that it does not bother the algorithm.
    translator = str.maketrans('', '', string.punctuation)
    st = st.translate(translator)
    left = 0            # Starting from the first index
    right = len(st) - 1 # Starting from last index

    # Loop until the pointers have met
    while left < right:
        char = st[left]
        ch = st[right]
        # If the characters at both places aren't same, return False
        if char != ch:
            return False

        # Move pointers closer
        left += 1
        right -= 1

    # return true if no different characters found
    # Time complexity: O(n) => All the operations are linear, no nesting
    # Space complexity: O(1) as we are not storing anything additional
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