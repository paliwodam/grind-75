
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len = 20
        n = len(s)
        words = set(wordDict)
        memo = [[None for _ in range(max_len)] for _ in range(n)]

        def recur(i, j):
            if j - i > max_len -1 or i >= n or j > n:
                return False

            if memo[i][j-i-1] is None:
                if j == n and s[i:j] in words:
                    memo[i][j-i-1] = True
                    return memo[i][j-i-1]
                if j > n:
                    memo[i][j-i-1] = False
                    return memo[i][j-i-1]
                
                if s[i:j] in words:
                    memo[i][j-i-1] = recur(i, j+1) or recur(j, j+1)
                else:
                    memo[i][j-i-1] = recur(i, j+1)
            return memo[i][j-i-1]
        return recur(0, 1)