# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        count = Counter(t)

        i, j = 0, 0
        while j < n:
            if s[j] in t:
                count[s[j]] -= 1
                if count[s[j]] >= 0:
                    m -= 1
                if m == 0:
                    break
            j += 1

        if j == n:
            return ""

        while i < n:
            if s[i] in t:
                if count[s[i]] == 0:
                    break
                else:
                    count[s[i]] += 1
            i += 1
        
        k, l = i, j
        j += 1

        while i < n and j < n:
            if s[j] in t:
                count[s[j]] -= 1
            while s[i] not in t or count[s[i]] < 0:
                if s[i] in t:
                    count[s[i]] += 1
                i += 1
            if j - i < l - k:
                k, l = i, j
            j += 1
        
        return s[k:l+1]
        