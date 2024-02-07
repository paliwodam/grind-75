# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
            if cnt[num] > n/2:
                return num
        return None