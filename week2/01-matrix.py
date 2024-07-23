# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.

from queue import PriorityQueue
from typing import List
from math import inf

class Solution:

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        adjacents = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        distances = [[inf for _ in range(m)] for _ in range(n)]

        queue = PriorityQueue()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0: queue.put((0, i, j))

        while not queue.empty():
            dist, i, j = queue.get()
            if 0 <= i < n and 0 <= j < m and dist < distances[i][j]:
                distances[i][j] = dist
                for x, y in adjacents:
                    queue.put((dist + 1, i+x, j+y))
        
        return distances
                
                    

        



            