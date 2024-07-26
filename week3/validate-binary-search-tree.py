# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
    
        queue = []
        queue.append((root, None, None))

        while len(queue) > 0:
            node, left, right = queue.pop()
            if node.left:
                val =  node.left.val
                if val < node.val and (not left or left < val):
                    queue.append((node.left, left, node.val))
                else:
                    return False
                    
            if node.right:
                val = node.right.val
                if val > node.val and (not right or right > val):
                    queue.append((node.right, node.val, right))
                else:
                    return False
        
        return True
        