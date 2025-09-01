# This file has all the problems in the Two Pointers
# section of the NeetCode150 with the explanations.

import string

# Problem-1:
def isPalindrome(s):
    """
   Valid Palindrome - Check if a string is a palindrome ignoring case and non-alphanumeric characters.
   Args:
       s: Input string to check
   Returns:
       bool: True if the string is a valid palindrome, False otherwise
    """
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
    """
    Two Sum II - Input Array Is Sorted
    Find two numbers in a sorted array that add up to target.
    Args:
        numbers: Sorted array of integers
        target: Target sum to find
    Returns:
        List[int]: 1-indexed positions of the two numbers, or None if not found
        """
    left = 0  # Start pointer at beginning
    right = len(numbers) - 1  # End pointer at end

    while left < right:  # Continue until pointers meet
        num1 = numbers[left]  # Left number
        num2 = numbers[right]  # Right number
        current_sum = num1 + num2

        if current_sum == target:
            # Found the target sum, return 1-indexed positions
            return [left + 1, right + 1]
        elif current_sum > target:
            # Sum too large, move right pointer left to decrease sum
            right -= 1
        else:
            # Sum too small, move left pointer right to increase sum
            left += 1

    # Time Complexity: O(n) - Single pass through array with two pointers
    # Space Complexity: O(1) - Only using constant extra space
    return None  # No valid pair found

def threeSum(nums):
    """
    3Sum - Find all unique triplets that sum to zero.

    Args:
        nums: Array of integers

    Returns:
        List[List[int]]: List of unique triplets that sum to zero
    """
    triples = []  # Store result triplets
    nums.sort()  # Sort array to enable two-pointer technique and handle duplicates

    for i, num in enumerate(nums):
        # Skip duplicate values for the first number to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Use two-pointer approach for the remaining two numbers
        left = i + 1  # Start after current element
        right = len(nums) - 1  # Start from end

        while left < right:
            curr_sum = num + nums[left] + nums[right]

            if curr_sum == 0:
                # Found a valid triplet
                triples.append([num, nums[left], nums[right]])
                left += 1
                right -= 1

                # Skip duplicate values for left pointer
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicate values for right pointer
                while right > left and nums[right] == nums[right + 1]:
                    right -= 1

            elif curr_sum > 0:
                # Sum too large, move right pointer left
                right -= 1
            else:
                # Sum too small, move left pointer right
                left += 1

    # Time Complexity: O(n²) - O(n log n) for sorting + O(n²) for nested loops
    # Space Complexity: O(1) - Not counting output array, only constant extra space
    return triples


def maxArea(heights):
    """
    Container With Most Water
    Find the maximum area that can be formed by two vertical lines.
    Args:
        heights: Array of integers representing line heights
    Returns:
        int: Maximum water area that can be contained
    """
    maxA = 0  # Track maximum area found
    left = 0  # Left boundary pointer
    right = len(heights) - 1  # Right boundary pointer

    while left < right:
        # Calculate current area: width × height (limited by shorter line)
        height = min(heights[left], heights[right])  # Water level limited by shorter line
        width = right - left  # Distance between lines
        currArea = height * width  # Current container area
        maxA = max(maxA, currArea)  # Update maximum area

        # Move the pointer with smaller height inward
        # This gives us the best chance to find a larger area
        if heights[left] > heights[right]:
            right -= 1  # Right line is shorter, move it inward
        elif heights[left] < heights[right]:  # Fixed syntax error: was heights[left < heights[right]]
            left += 1  # Left line is shorter, move it inward
        else:
            # Heights are equal, move both pointers
            # Moving either one alone won't help since height stays the same
            # and width decreases, so we might as well move both
            left += 1
            right -= 1

    # Time Complexity: O(n) - Single pass with two pointers
    # Space Complexity: O(1) - Only using constant extra space
    return maxA

if __name__ == '__main__':
    s = "Was it a car or a cat I saw?"
    print(isPalindrome(s))