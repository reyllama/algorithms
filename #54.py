"""
2023.04.07
"""
"""
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.
"""
class Solution:
    def rotate(self, matrix):
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        out = [None for _ in range(n)]
        for r in range(n):
            out[r] = [matrix[k][n-r-1] for k in range(m)]
        return out

    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res += matrix[0]
            matrix = self.rotate(matrix[1:])
        return res

"""
Time > 90%, Memory > 70.71%
Take the first row out and rotate the matrix counter-clock-wise until no row is left.
"""