# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']
        bracket_pairs = dict(zip(open_brackets, close_brackets))

        opened_brackets = []
        for bracket in s:
            if bracket in open_brackets:
                opened_brackets.append(bracket)
            if bracket in close_brackets:
                if len(opened_brackets) == 0:
                    return False
                last_open = opened_brackets.pop()
                if bracket != bracket_pairs[last_open]:
                    return False
                    
        if len(opened_brackets) != 0:
            return False
        return True
