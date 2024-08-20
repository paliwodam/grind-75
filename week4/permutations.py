# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def extend_sequence(sequence):
            result = []
            for num in nums:
                if num not in sequence:
                    result.append(sequence + (num, ))
            return result 

        n = len(nums)
        permutations = [(num, ) for num in nums]

        while len(permutations[0]) < n:
            new_permutations = []
            for sequence in permutations:
                new_permutations += extend_sequence(sequence)
            permutations = new_permutations

        return [list(x) for x in permutations]
        