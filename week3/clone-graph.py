
## Given a reference of a node in a connected undirected graph.
## Return a deep copy (clone) of the graph.
##Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.



# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.clone_DFS(node)

    def clone_DFS(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if getattr(node, 'clone', None):
            return node.clone

        clone = Node(node.val)
        node.clone = clone
        for neigh in node.neighbors:
            clone.neighbors.append(self.clone_DFS(neigh))
        return clone

