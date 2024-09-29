## Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, nums_sum = len(nums), sum(nums)
        if nums_sum % 2 == 1: return False
        half = nums_sum // 2

        memo = [[False for _ in range(n)] for _ in range(half + 1)]
        for i in range(n): memo[0][i] = True

        for i in range(1, n):
            for j in range(1, half+1):
                memo[j][i] = memo[j][i-1]
                if j - nums[i] >= 0:
                    memo[j][i] = memo[j][i] or memo[j-nums[i]][i-1]
        
        return any(memo[half])