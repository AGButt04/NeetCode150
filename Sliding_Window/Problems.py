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
    # Space Complexity: O(min(m,n)) - HashMap stores at most min(alpha
    return maxLength
