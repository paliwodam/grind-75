# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        n = len(alphanumeric)
        mid = n // 2

        return alphanumeric[:mid] == alphanumeric[:n-mid-1:-1]