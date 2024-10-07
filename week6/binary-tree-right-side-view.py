# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

from typing import Optional
from queue import PriorityQueue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = PriorityQueue()
        current_level = 0
        queue.put((0, 0, root))
        result = []
        while not queue.empty():
            level, val, node = queue.get()
            if node is None: continue
            if level == current_level:
                result.append(node.val)
                current_level += 1
            if node.right: 
                queue.put((level+1, val*2+1, node.right))
            if node.left: 
                queue.put((level+1, val*2+2, node.left))

        return result


            