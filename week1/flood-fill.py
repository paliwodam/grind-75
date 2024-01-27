# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
# Return the modified image after performing the flood fill.

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def fill(i, j, start_col):
            if i < 0 or i >= len(image):
                return
            if j < 0 or j >= len(image[0]):
                return  
            if image[i][j] == start_col:
                image[i][j] = color
                fill(i+1, j, start_col)
                fill(i-1, j, start_col)
                fill(i, j+1, start_col)
                fill(i, j-1, start_col)
        
        if image[sr][sc] == color:
            return image
        
        fill(sr, sc, image[sr][sc])
        
        return image

