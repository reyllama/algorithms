"""
2023.04.06
"""
"""
48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # elements that are altered by row <- column operation (that affects later operations)
        cache = [[] for _ in range(n)]
        # Replace each row with corresponding column, but chunked to consider prior replacements
        for r in range(n):
            for c in range(r+1, n):
                cache[c].append(matrix[r][c])
            # Concatenate column chunk and cache chunk
            matrix[r] = [matrix[n-k-1][r] for k in range(n)][:n-r] + cache[r][::-1]

"""
Time > 67.85%, Memory > 97.13%
"""