"""
2023.04.13
"""
"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        steps = [None] * n
        steps[0], steps[1] = 1, 2
        for i in range(2, n):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[-1]

"""
Time > 98.12%
Memory > 43.94%
"""