## Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, nums_sum = len(nums), sum(nums)
        if nums_sum % 2 == 1: return False
        half = nums_sum // 2

        all_sums = set([0])
        
        for num in nums:
            for el in list(all_sums):
                all_sums.add(el + num)
        
        return half in all_sums