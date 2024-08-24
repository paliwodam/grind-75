# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pointer = -1
        for color in [0, 1, 2]:
            for i in range(n):
                if nums[i] == color:
                    pointer += 1
                    nums[pointer], nums[i] = nums[i], nums[pointer]
        