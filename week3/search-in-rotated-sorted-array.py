# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def b_search(start, end, target, nums):
            if end < start:
                return -1
            if end - start == 1:
                if nums[start] == target: return start
                if nums[end] == target: return end
                return -1
                
            middle = (end - start) // 2 + start
            if nums[middle] == target:
                return middle

            if nums[middle] < nums[start] and target >= nums[start]:
                return b_search(start, middle, target, nums)
            if nums[middle] > nums[end] and target <= nums[end]:
                return b_search(middle, end, target, nums)

            if target > nums[middle]:
                    return b_search(middle+1, end, target, nums)
            if target < nums[middle]:
                return b_search(start, middle-1, target, nums)

            return -1

        return b_search(0, len(nums)-1, target, nums)