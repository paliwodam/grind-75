# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters_cnt = defaultdict(int)
        for letter in magazine:
            letters_cnt[letter] += 1

        for letter in ransomNote:
            letters_cnt[letter] -= 1
            if letters_cnt[letter] < 0:
                return False
        
        return True