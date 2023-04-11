"""
2023.04.11
"""
"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""
class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda interval: interval[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(interval[1], res[-1][1])]
            else:
                res.append(interval)
        return res

"""
Time > 99.51%, Memory > 98.79%
Sort the intervals by their starting point, so that we only consider one condition (whether their start point is lower than the previous end point)
If we do not sort at first, we have to compare an incoming interval with all previous intervals in `res`, making the algorithm close to O(N^2).
"""