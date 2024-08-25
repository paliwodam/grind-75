# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.values[key]
        left, right = 0, len(values)-1
        while left <= right:
            middle = (left + right) // 2
            if values[middle][0] == timestamp:
                return values[middle][1]
            elif values[middle][0] < timestamp:
                left = middle + 1
            else:
                right = middle - 1
        if left == 0:
            return ""
        return values[left-1][1]
        
        
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)