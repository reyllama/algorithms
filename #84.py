"""
2023.05.16
"""
"""
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        curMax = 0
        stack = []
        for height in heights+[-1]:
            streak = 0
            while stack and stack[-1][1] >= height:
                w, h = stack.pop()
                streak += w
                curMax = max(curMax, streak*h)
            stack.append([streak+1, height])
            print(height, curMax)
        return curMax

"""
<Idea>
Keep a monotonic stack, where if a new number is smaller than the last element, we start calculating curMax.
(As long as the number keeps increasing, it is GUARANTEED that the rectangle expands.
Use the variable streak very cleverly, which indicates how much width can be supported at current height level.
If height gets smaller, the streak gets larger as we are trading off height for width.
"""