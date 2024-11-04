# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def backtrack(k, x, y):
            if board[x][y] != word[k]:
                return False
            if k == len(word)-1:
                return True

            tmp = board[x][y]
            board[x][y] = None
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= x + i < m and 0 <= y + j < n:
                    if backtrack(k+1, x+i, y+j):
                        return True

            board[x][y] = tmp
            return False

        for x in range(m):
            for y in range(n):
                if backtrack(0, x, y):
                    return True
        return False