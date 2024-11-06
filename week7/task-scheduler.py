# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.
# Return the minimum number of CPU intervals required to complete all tasks.

from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        max_val = max(cnt.values())
        max_val_cnt = len([val for val in cnt.values() if val == max_val])

        return max(len(tasks), (max_val - 1) * (n + 1) + max_val_cnt)