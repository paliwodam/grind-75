# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the  frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

from typing import List 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        memo = [None] * (target + 1)
        memo[0] = [[]]

        for i in range(target):
            if memo[i] is not None:
                for combinations in memo[i]:
                    for x in candidates:
                        min_val =  max(combinations) if len(combinations) > 0 else 0
                        if i + x <= target and x >= min_val:
                            if memo[i + x] is None:
                                memo[i + x] = []
                            memo[i + x].append((combinations.copy() + [x]))
        
        return memo[target]