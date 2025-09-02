# This file has all the problems in the Sliding Window
# section of the NeetCode150 with the explanations.

def maxProfit(prices):
        maxProfit = 0
        buyPrice = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > buyPrice:
                currProfit = prices[i] - buyPrice
                maxProfit = max(currProfit, maxProfit)
            else:
                buyPrice = prices[i]

        return maxProfit


def lengthOfLongestSubstring(s):
    maxLength = 0
    cache = {}
    left = 0

    for right in range(len(s)):
        if s[right] in cache:
            left = max(cache[s[right]] + 1, left)

        cache[s[right]] = right
        length = right - left + 1
        maxLength = max(maxLength, length)

    return maxLength
