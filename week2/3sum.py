# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        triples = []
        i = 0
        while i < n-1:
            j = i + 1
            k = n - 1
            while j < k:
                triple_sum = nums[i] + nums[j] + nums[k]
                if triple_sum == 0:
                    triples.append([nums[i], nums[j], nums[k]])
                    while j + 1 < k and nums[j] == nums[j+1]: j += 1
                    j += 1
                elif triple_sum > 0:
                    k -= 1
                else:
                    j += 1
            while i + 1 < k and nums[i] == nums[i+1]: i += 1
            i += 1
        return triples