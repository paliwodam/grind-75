# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        neigh = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = [[]]

        def add_neighbours_to_queue(x, y, time):
            for i, j in neigh:
                if 0 <= x+i < n and 0 <= y+j < m:
                    queue[-1].append((x+i, y+j, time))

        for x in range(n):
            for y in range(m):
                if grid[x][y] == 2:
                    add_neighbours_to_queue(x, y, 2)

        while len(queue[0]) > 0:
            queue.append([])
            for x, y, time in queue[0]:
                if grid[x][y] == 1:
                    grid[x][y] = time + 1
                    add_neighbours_to_queue(x, y, time + 1)
            queue.pop(0)

        time = 0
        for row in grid:
            for cell in row:
                time = max(time, cell)
                if cell == 1: 
                    return -1
        
        return max(0, time - 2)
    