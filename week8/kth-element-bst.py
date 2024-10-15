# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth = None
        def DFS(node, prev):
            if node is None:
                return 0
            left = DFS(node.left, prev)
            curr = left + 1 if left != 0 else prev + 1
            nonlocal kth
            if curr == k:
                kth = node.val
                
            right = DFS(node.right, curr)
            return right or curr
        
        DFS(root, 0)
        return kth

