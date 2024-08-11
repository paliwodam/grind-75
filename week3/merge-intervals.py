# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        start_min, end_max = intervals[0]

        for start_i, end_i in intervals:
            if start_min <= start_i <= end_max:
                end_max = max(end_max, end_i)
            else:
                merged.append([start_min, end_max])
                start_min, end_max = start_i, end_i


        if len(merged) == 0 or start_min != merged[-1][0] or end_max != merged[-1][1]:
            merged.append([start_min, end_max])
        
        return merged


        