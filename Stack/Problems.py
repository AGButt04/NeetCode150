# This file has all the problems in the Sliding Window
# section of the NeetCode150 with the explanations.

def isValid(s):
    stack = []

    for parentheses in s:
        if parentheses == '{' or parentheses == '(' or parentheses == '[':
            stack.append(parentheses)
        elif stack:
            if parentheses == '}' and stack[-1] == '{':
                stack.pop()
            elif parentheses == ')' and stack[-1] == '(':
                stack.pop()
            elif parentheses == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
        else:
            return False

    # Time Complexity: O(n) as the loop only walks through the string once
    # Space Complexity: 0(n) as we are keeping track of opening parentheses

    return len(stack) == 0

class MinStack:
    # O(1) operations for each function
    # O(n) space as we are maintaining two stacks
    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, val):
        self.stack.append(val)
        if self.minimums:
            self.minimums.append(min(self.minimums[-1], val))
        else:
            self.minimums.append(val)

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.minimums.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        if self.minimums:
            return self.minimums[-1]
        return None