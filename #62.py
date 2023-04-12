"""
2023.04.12
"""
"""
62. Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[1]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                board[i][j] = board[i-1][j] + board[i][j-1]
        return board[-1][-1]

"""
Time > 91.7%, Memory > 96.91%
"""