# This file has all the problems in the 1-D Dynammic Programming
# section of the NeetCode150 with the explanations.

def climbStairs(self, n):
    memo = {}

    def steps(memo, num):
        if num in memo:
            return memo[num]
        if num < 0:
            return 0
        if num == 0:
            return 1

        one_step = steps(memo, num - 1)
        two_step = steps(memo, num - 2)

        total = one_step + two_step
        memo[num] = total

        return total

    return steps(memo, n)

