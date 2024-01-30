# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = set()
        max_length = 0
        for c in s:
            if c in letters:
                letters.remove(c)
                max_length += 2
            else:
                letters.add(c)

        if len(letters) > 0:
            max_length += 1
        return max_length