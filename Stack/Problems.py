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