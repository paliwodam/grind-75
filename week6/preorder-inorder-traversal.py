# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        head = TreeNode(preorder[0])

        prev_node = head
        possible_right_child_of = [head]

        indexes = {x : idx for idx, x in enumerate(inorder)}
        parents = {head: (None, None)}

        def left(node1, node2):
            return indexes[node1.val] < indexes[node2.val]
        
        def right(node1, node2):
            node = node1
            while True:
                parent, left_or_right = parents[node]
                if parent is None:
                    return indexes[node2.val] > indexes[node1.val]
                if left_or_right == "l":
                    if indexes[node2.val] > indexes[parent.val]:
                        return False
                elif left_or_right == "r":
                    if indexes[node2.val] < indexes[parent.val]:
                        return False
                node = parent

        idx = 1
        while idx < n:
            curr_node = TreeNode(preorder[idx])
            if left(prev_node, curr_node):
                prev_node.left = curr_node
                parents[curr_node] = (prev_node, "l")
            
            while curr_node not in parents and len(possible_right_child_of) > 0:
                node = possible_right_child_of.pop(-1)
                if right(node, curr_node):
                    node.right = curr_node
                    parents[curr_node] = (node, "r")

            prev_node = curr_node
            possible_right_child_of.append(curr_node)
            idx += 1
        return head
