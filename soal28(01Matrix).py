# https://leetcode.com/problems/01-matrix/
# https://lenchen.medium.com/leetcode-542-01-matrix-b85e06193ec8

from collections import deque

class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        # approach: use BFS start from all 0s to update all non-zero elements

        m = len(matrix)
        n = len(matrix[0])

        queue = deque()

        # for reusing original matrix, convert 1 to infinity at initialization
        for i, row in enumerate(matrix):
            for j, ele in enumerate(row):
                if ele:
                    matrix[i][j] = float('inf')
                else:
                    queue.append((i, j))

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while queue:
            for count in range(len(queue)):
                i, j = queue.popleft()

                for x, y in directions:
                    row, col = i + x, j + y

                    if -1 < row < m and -1 < col < n and matrix[row][col] > matrix[i][j] + 1:
                        matrix[row][col] = matrix[i][j] + 1
                        queue.append((row, col))

        return matrix