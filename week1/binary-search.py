# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_idx = 0
        end_idx = len(nums) - 1

        while start_idx <= end_idx:
            pivot = (end_idx - start_idx) // 2 + start_idx
            if nums[pivot] == target:
                return pivot
            if nums[pivot] > target:
                end_idx = pivot-1
            if nums[pivot] < target:
                start_idx = pivot+1
        
        return -1 
