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