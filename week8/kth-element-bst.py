# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node, stack = root, []
        n = 0

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            n += 1 

            if n == k:
                return node.val

            node = node.right