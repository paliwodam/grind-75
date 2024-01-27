# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.visited = False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow_pointer = head
        fast_pointer = head.next

        while slow_pointer is not None and fast_pointer is not None and slow_pointer != fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
            if fast_pointer != None:
                fast_pointer = fast_pointer.next

        
        if slow_pointer is not None and fast_pointer is not None and slow_pointer == fast_pointer:
            return True
        else:
            return False