# This file has all the problems in the Sliding Window
# section of the NeetCode150 with the explanations.

def isValid(s):
    """
    Valid Parentheses - Check if parentheses are properly matched and nested.
    Approach: Use stack to track opening brackets, match with closing brackets.
    """

    stack = []

    for parentheses in s:
        # Push opening brackets onto stack
        if parentheses == '{' or parentheses == '(' or parentheses == '[':
            stack.append(parentheses)
        elif stack:  # Closing bracket and stack not empty
            # Check if closing bracket matches most recent opening bracket
            if parentheses == '}' and stack[-1] == '{':
                stack.pop()
            elif parentheses == ')' and stack[-1] == '(':
                stack.pop()
            elif parentheses == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False  # Mismatched brackets
        else:
            return False  # Closing bracket with no opening bracket

    # Time Complexity: O(n) - single pass through string
    # Space Complexity: O(n) - stack stores opening brackets

    return len(stack) == 0  # Valid if all brackets matched

class MinStack:
    """
    Min Stack - Stack supporting push, pop, top, and getMin in O(1) time.
    Approach: Use auxiliary stack to track minimum at each level.

    All operations: O(1) time complexity
    Space complexity: O(n) for maintaining two stacks
    """

    def __init__(self):
        self.stack = []  # Main stack for values
        self.minimums = []  # Auxiliary stack tracking minimums

    def push(self, val):
        """Add element to stack and update minimum tracking."""
        self.stack.append(val)
        # Track minimum: either current val or previous minimum
        if self.minimums:
            self.minimums.append(min(self.minimums[-1], val))
        else:
            self.minimums.append(val)  # First element

    def pop(self):
        """Remove top element and corresponding minimum."""
        if self.stack:
            self.stack.pop()
            self.minimums.pop()  # Keep stacks synchronized

    def top(self):
        """Return top element without removing it."""
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        """Return minimum element in current stack."""
        if self.minimums:
            return self.minimums[-1]
        return None

def evalRPN(tokens):
    """
        Evaluate Reverse Polish Notation
        Calculate result of expression in postfix notation.

        Approach: Use stack to store operands, apply operators when encountered.
    """
    stack = []

    for string in tokens:
        try:
            # Try to convert to number
            strNum = int(string)
            stack.append(strNum)
        except ValueError:
            # It's an operator - pop two operands
            right = stack.pop()  # Second operand
            left = stack.pop()  # First operand

            if string == "+":
                newNum = left + right
            elif string == "-":
                newNum = left - right
            elif string == "*":
                newNum = left * right
            else:  # Division
                newNum = int(left / right)  # Truncate toward zero

            stack.append(newNum)

    # Time Complexity: O(n) - single pass through tokens
    # Space Complexity: O(n) - stack stores operands
    return stack[-1]  # Final result

def generateParenthesis(n):
    """
        Generate Parentheses
        Generate all valid combinations of n pairs of parentheses.
        Approach: Backtracking with constraints on open/close counts.
    """
    parentheses = []
    recurse("", 0, 0, parentheses, n)
    return parentheses


def recurse(st, openCount, closeCount, parentheses, n):
    """
    Recursive helper for generating valid parentheses combinations.
    Args:
        st: Current string being built
        openCount: Number of '(' added so far
        closeCount: Number of ')' added so far
        parentheses: Result list to populate
        n: Target number of pairs
    """
    # Pruning: invalid states
    if openCount > n or openCount < closeCount:
        return

    # Base case: complete valid combination
    if len(st) == n * 2:
        parentheses.append(st)
        return

    # Try adding opening parenthesis
    recurse(st + "(", openCount + 1, closeCount, parentheses, n)
    # Try adding closing parenthesis
    recurse(st + ")", openCount, closeCount + 1, parentheses, n)
    # Time Complexity: O(4^n / sqrt(n)) - Catalan number bounds
    # Space Complexity: O(n) - recursion depth and string length

def dailyTemperatures(temperatures):
    """
        Daily Temperatures
        Find how many days until a warmer temperature for each day.
        Approach: Monotonic stack to track indices of unresolved temperatures.
    """
    stack = []  # Store indices of temperatures waiting for warmer day
    result = [0] * len(temperatures)  # Initialize with 0s (no warmer day)

    for index, temp in enumerate(temperatures):
        # Process all previous temperatures that are cooler than current
        while stack and temperatures[stack[-1]] < temp:
            prevIndex = stack.pop()  # Index of cooler temperature
            days = index - prevIndex  # Days between temperatures
            result[prevIndex] = days

        stack.append(index)  # Add current day to stack

    # Time Complexity: O(n) - each index pushed/popped at most once
    # Space Complexity: O(n) - stack and result array
    return result


def carFleet(target, position, speed):
    """
    Clean stack-based solution for car fleet problem.
    Stack stores the time to destination for the leading car of each fleet.
    """
    stack = []
    sortedPositions = [(p, s) for p, s in zip(position, speed)]
    sortedPositions.sort(reverse=True)  # Sort by position, closest to target first

    for p, s in sortedPositions:
        distance = (target - p) / s  # Time to reach destination
        stack.append(distance)

        # If current car is faster than the car ahead, it will catch up
        # Remove the faster car's time since they'll form one fleet
        if len(stack) >= 2:
            if stack[-1] <= stack[-2]:
                stack.pop()

    # Time complexity: O(n) for iterating through the array and sorting O (log) => O(n log n)
    # Space complexity: O(n) for keeping track of the stack and the sorted array
    return len(stack)  # Number of fleets = number of leading cars


def largestRectangleArea(heights):
    stack = []  # Stack stores indices of heights in increasing order
    maxArea = 0

    for i, h in enumerate(heights):
        # When current height is shorter, calculate rectangles for taller bars
        # Pop all bars taller than current height
        while stack and heights[stack[-1]] > h:
            currArea = heightCheck(i, stack, heights)
            maxArea = max(maxArea, currArea)

        stack.append(i)

    # Process remaining bars (all in increasing order)
    # Use array length as right boundary since no shorter bar found
    while stack:
        currArea = heightCheck(len(heights), stack, heights)
        maxArea = max(maxArea, currArea)

    # Time Complexity: O(n) => As walks through the array once and pops indices once
    # Space Complexity:  O(n) => As we are keeping track of the stack (indices)
    return maxArea


def heightCheck(rightBound, stack, heights):
    currIndex = stack.pop()  # Index of bar we're calculating rectangle for
    height = heights[currIndex]

    # Calculate width: distance between left and right boundaries
    # Left boundary = top of stack (last shorter bar), Right boundary = current position
    if stack:
        width = rightBound - stack[-1] - 1  # Exclude the boundary bars
    else:
        width = rightBound  # No left boundary, rectangle extends to start

    return height * width




