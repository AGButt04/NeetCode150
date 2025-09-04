# This file has all the problems in the Sliding Window
# section of the NeetCode150 with the explanations.

def maxProfit(prices):
    """
    Best Time to Buy and Sell Stock
    Find the maximum profit from buying and selling stock once.
    Args:
        prices: List of stock prices where prices[i] is price on day i
    Returns:
        int: Maximum profit achievable, 0 if no profit possible
    """
    maxProfit = 0  # Track maximum profit found so far
    buyPrice = prices[0]  # Start with first day as potential buy price

    # Iterate through prices starting from day 1
    for i in range(1, len(prices)):
        if prices[i] > buyPrice:
            # Current price is higher than our buy price - potential profit
            currProfit = prices[i] - buyPrice  # Calculate profit if we sell today
            maxProfit = max(currProfit, maxProfit)  # Update max profit if better
        else:
            # Current price is lower - update buy price for better future opportunity
            buyPrice = prices[i]

    # Time Complexity: O(n) - Single pass through the array
    # Space Complexity: O(1) - Only using constant extra variables
    return maxProfit

def lengthOfLongestSubstring(s):
    """
    Longest Substring Without Repeating Characters
    Find the length of the longest substring without repeating characters.
    Args:
        s: Input string to analyze
    Returns:
        int: Length of longest substring with all unique characters
    """
    maxLength = 0  # Track maximum substring length found
    cache = {}  # HashMap: character -> most recent index
    left = 0  # Left boundary of sliding window

    # Expand window by moving right pointer
    for right in range(len(s)):
        if s[right] in cache:
            # Duplicate character found - shrink window from left
            # Move left to position after the previous occurrence of this character
            # Use max() to ensure left pointer never moves backward
            left = max(cache[s[right]] + 1, left)

        # Update character's most recent position
        cache[s[right]] = right

        # Calculate current window length
        length = right - left + 1
        maxLength = max(maxLength, length)

    # Time Complexity: O(n) - Each character visited at most twice (once by each pointer)
    # Space Complexity: O(min(m,n)) - HashMap stores at most min(alphabet_size, string length)
    return maxLength

def checkInclusion(s1, s2):
    """
    Permutation in String (Sliding Window)
    Check if any permutation of s1 is a substring of s2.
    Args:
        s1: Pattern string to find permutation of
        s2: Text string to search in
    Returns:
        bool: True if any permutation of s1 exists as substring in s2
    """
    # Early termination: s1 cannot fit in s2
    if len(s1) > len(s2):
        return False

    s1Map = {}  # Character frequency map for s1 (target pattern)
    s2Map = {}  # Character frequency map for current sliding window
    length = len(s1)  # Fixed window size

    # Build frequency map for s1 (the pattern we're looking for)
    for char in s1:
        s1Map[char] = s1Map.get(char, 0) + 1

    # Initialize sliding window with first 'length' characters of s2
    for i in range(length):
        s2Map[s2[i]] = s2Map.get(s2[i], 0) + 1

    # Slide the window through the rest of s2
    for i in range(length, len(s2)):
        # Check if current window matches s1's character distribution
        if s1Map == s2Map:
            return True

        # Slide window: remove leftmost character (going out of window)
        char = s2[i - length]  # Character leaving the window
        s2Map[char] = s2Map[char] - 1
        if s2Map[char] == 0:
            del s2Map[char]  # Remove key when count reaches 0 for clean comparison

        # Add new rightmost character (entering the window)
        s2Map[s2[i]] = s2Map.get(s2[i], 0) + 1

    # Time Complexity: O(n + m) where n = len(s1), m = len(s2)
    # - Building s1Map: O(n)
    # - Initial window setup: O(n)
    # - Sliding through remaining characters: O(m - n)
    # - HashMap comparisons: O(1) average case due to limited alphabet size
    # Space Complexity: O(n) for the frequency maps (at most 26 characters each)

    # Check the final window position (crucial - don't forget this!)
    return s1Map == s2Map

def characterReplacement(s, k):
    """
    Longest Repeating Character Replacement
    Find length of longest substring with same characters after at most k replacements.
    Args:
        s: Input string
        k: Maximum number of character replacements allowed
    Returns:
        int: Length of longest valid substring
    """
    count = {}  # Character frequency map for current window
    maxlen = 0  # Maximum valid window size found
    maxfreq = 0  # Highest frequency of any character in current window
    left = 0  # Left boundary of sliding window

    # Expand window by moving right pointer
    for right in range(len(s)):
        # Add new character to window
        count[s[right]] = count.get(s[right], 0) + 1

        # Update maximum frequency (most common character in current window)
        maxfreq = max(maxfreq, count[s[right]])

        # Check if current window is valid
        # Window is valid if: (window_size - most_frequent_count) <= k
        # This means we need at most k replacements to make all characters the same
        while (right - left + 1) - maxfreq > k:
            # Window invalid: shrink from left until valid again
            count[s[left]] -= 1  # Remove leftmost character
            left += 1  # Move left boundary right

            # Note: We don't update maxfreq here for optimization
            # It's okay to keep a slightly higher maxfreq because:
            # 1. It only makes the condition more lenient (still correct)
            # 2. Recalculating maxfreq would make it O(n) per iteration

        # Update maximum valid window size found
        maxlen = max(maxlen, right - left + 1)

    # Time Complexity: O(n) where n = len(s)
    # - Outer loop runs n times (right pointer)
    # - Inner while loop: each left pointer position visited at most once
    # - Total: O(n) amortized
    # Space Complexity: O(min(n, 26)) = O(1) for the frequency map
    # - At most 26 different characters (English alphabet)
    return maxlen

def minWindow(s, t):
    tMap = {}
    sMap = {}
    left = 0
    minWindow = ""

    for char in t:
        tMap[char] = tMap.get(char, 0) + 1

    need = len(tMap)
    have = 0
    for right, char in enumerate(s):
        if char in tMap:
            sMap[char] = sMap.get(char, 0) + 1
            if sMap[char] == tMap[char]:
                have += 1

        while need == have:
            if not minWindow or (right - left + 1) < len(minWindow):
                minWindow = s[left: right + 1]

            ch = s[left]
            if ch in sMap:
                sMap[ch] -= 1
                if sMap[ch] < tMap[ch]:
                    have -= 1
                if sMap[ch] == 0:
                    del sMap[ch]

            left += 1

    return minWindow

def maxSlidingWindow(nums, k):
    maxes = []
    currMax = 0
    left = 0

    for i in range(k):
        currMax = max(currMax, nums[i])

    for right in range(k, len(nums)):
        maxes.append(currMax)
        left += 1

        if nums[right] > currMax:
            currMax = nums[right]
        if nums[left - 1] == currMax:
            currMax = max(nums[left: right + 1])

    maxes.append(currMax)
    return maxes


