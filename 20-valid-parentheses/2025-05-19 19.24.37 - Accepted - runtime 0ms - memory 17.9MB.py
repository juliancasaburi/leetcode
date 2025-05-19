from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize a deque to use as a stack
        stack = deque()

        brackets = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        for bracket in s:
            # If the character is an opening bracket, push it onto the stack
            if bracket in brackets:
                stack.append(bracket)
            # If it's a closing bracket and there are opening brackets in the stack
            elif len(stack) != 0:
                # Pop the last unmatched opening bracket
                open_bracket = stack.pop()
                # Check if the closing bracket matches the expected one
                if bracket != brackets[open_bracket]:
                    return False  # Found a mismatch
            else:
                # Found a closing bracket but there was no corresponding opening bracket
                return False

        # If stack is empty at the end, no unmatched opening brackets remain
        return len(stack) == 0
