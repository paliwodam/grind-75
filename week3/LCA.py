# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def ancestor(self, root, p, q):
        if root is None:
            return None, None

        left_p_LA, left_q_LA = self.ancestor(root.left, p, q)
        right_p_LA, right_q_LA = self.ancestor(root.right, p, q)

        p_LA = left_p_LA or right_p_LA or (root if root == p else None)
        q_LA = left_q_LA or right_q_LA or (root if root == q else None)

        if p_LA is not None and q_LA is not None and p_LA != q_LA:
            return root, root
        return p_LA, q_LA

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_LA, q_LA = self.ancestor(root, p, q)
        if p_LA == q_LA:
            return p_LA
        return None

        