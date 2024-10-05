# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

 

from copy import deepcopy
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def extend_subsets(i, subsets):
            if i >= n:
                return subsets
            extended_subsets = deepcopy(subsets)
            for subset in extended_subsets:
                subset.append(nums[i])
            return extend_subsets(i+1, subsets + extended_subsets)

        return extend_subsets(0, [[]])

        