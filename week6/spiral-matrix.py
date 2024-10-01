# Given an m x n matrix, return all elements of the matrix in spiral order.

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len((matrix[0]))
        i,j,k,l = 0, n, 0, m 
        result = []

        def right(i, j, k, l):
            for idx in range(k, l-1):
                result.append(matrix[i][idx])

        def down(i, j, k, l):
            for idx in range(i, j-1):
                result.append(matrix[idx][l-1])

        def left(i, j, k, l):
            for idx in range(l-1, k, -1):
                result.append(matrix[j-1][idx])

        def up(i, j, k, l):
            for idx in range(j-1, i, -1):
                result.append(matrix[idx][k])

        while i < j-1 and k < l-1:
            r = right(i, j, k, l)
            d = down(i, j, k, l)
            lf = left(i, j, k, l)
            u = up(i, j, k, l)
            k += 1
            i += 1
            l -= 1
            j -= 1

        if k < l and len(result) < n * m:
            right(i, j, k, l+1)
        if i < j and len(result) < n * m:
            down(i+1, j+1, k, l)
        
        return result