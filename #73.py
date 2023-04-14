"""
2023.04.13
"""
"""
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        from collections import defaultdict
        zeros = defaultdict(list)
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros['row'].append(i)
                    zeros['col'].append(j)
        for row in zeros['row']:
            matrix[row] = [0] * n
        for col in zeros['col']:
            for r in range(m):
                matrix[r][col] = 0

"""
Time > 83.59%, Memory > 95.16%
"""