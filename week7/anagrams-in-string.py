# Given two strings s and p, return an array of all the start indices of p's 
# anagrams in s. You may return the answer in any order.

from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def idx(letter):
            return ord(letter) - ord("a")

        n, m = len(s), len(p)
        if n < m: return []
        p_count = [0 for _ in range(26)]
        current_count = [0 for _ in range(26)]

        for i in range(m):
            p_count[idx(p[i])] += 1
            current_count[idx(s[i])] += 1

        result = [0] if p_count == current_count else []
        for i in range(1, n-m+1):
            current_count[idx(s[i-1])] -= 1
            current_count[idx(s[i+m-1])] += 1
            if p_count == current_count:
                result.append(i)
        return result