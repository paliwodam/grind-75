# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        num_idx = {}
        for i in range(n):
            diff = target - nums[i]
            if diff in num_idx:
                return i, num_idx[diff]
            if nums[i] not in num_idx:
                num_idx[nums[i]] = i