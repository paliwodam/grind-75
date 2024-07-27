# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

from typing import List

class Solution:
    neigh = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def mark_island(self, x, y, grid: List[List[str]], visited: List[List[bool]]):
        if x < 0 or x >= len(grid):
            return
        if y < 0 or y >= len(grid[0]):
            return 
        if visited[x][y]:
            return 
        visited[x][y] = True

        if grid[x][y] == "1":
            for i, j in self.neigh:
                self.mark_island(x+i, y+j, grid, visited)


    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        island_count = 0
        for x in range(n):
            for y in range(m):
                if not visited[x][y] and grid[x][y] == "1":
                    island_count +=1
                    self.mark_island(x, y, grid, visited)
        
        return island_count

