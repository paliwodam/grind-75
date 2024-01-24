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
