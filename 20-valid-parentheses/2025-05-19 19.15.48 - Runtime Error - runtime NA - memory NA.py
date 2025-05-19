from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()

        brackets = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        for bracket in s:
            if bracket in brackets.keys():
                stack.append(bracket)
            else:
                open_bracket = stack.pop()
                if bracket != brackets[open_bracket]:
                    return False

        if len(stack) != 0:
            return False
        else:
            return True
