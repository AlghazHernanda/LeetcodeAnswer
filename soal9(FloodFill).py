# https://leetcode.com/problems/flood-fill/

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        if image == None or image[sr][sc] == newColor:
            return image
        
        self.fill(image, sr, sc, image[sr][sc], newColor)
        return image
    
    def fill(self, image, row, column, initial, newColor):

        if (
            row < 0 or row >= len(image) or 
            column < 0 or column >= len(image[0]) or 
            image[row][column] != initial
        ):
            return

        image[row][column] = newColor
        
        self.fill(image, row - 1, column, initial, newColor) # up
        self.fill(image, row + 1, column, initial, newColor) # down
        self.fill(image, row, column - 1, initial, newColor) # left
        self.fill(image, row, column + 1, initial, newColor) # right