"""
2023.04.03
"""
"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        cache = [len(height)] * max(height)
        ans, prev = 0, 0
        for i, h in enumerate(height):
            for k in range(prev+1, h+1):
                ans += max(i-cache[k-1]-1, 0)
            cache[:h] = [i] * h
            prev = h
        return ans

"""
Time Limit Exceeded. (318/322)
"""

class Solution:
    def trap(self, height):
        from collections import defaultdict
        map_ = defaultdict(list)
        for i, v in enumerate(height):
            map_[v].append(i)
        heights = sorted(list(map_.keys()))[::-1]

        prev_sum = 0
        prev = heights[0]
        prev_l, prev_r = map_[prev][0], map_[prev][-1]
        ans = 0

        for h in range(heights[0], 0, -1):
            if map_.get(h, None) is None:
                ans += offset
                continue
            prev_sum += len(map_[h])
            offset = max(max(map_[h][-1], prev_r) - min(map_[h][0], prev_l) -1 -(prev_sum-2), 0)
            ans += offset
            prev_l, prev_r = map_[h][0], map_[h][-1]
        return ans

"""
Time > 5.65%, Memory > 6.52%
Works, but not satisfactory at all
"""

class Solution:
    def trap(self, height):
        curMax, lMax, rMax = 0, [], []
        # curMax: current maximu value, either starting from left or right (refresh once left is done)
        # lMax: cumulative maximum value UNTIL the index
        # rMax: cumulative maximum value UNTIL the index, but starting from rightmost index.
        for h in height:
            if h > curMax:
                curMax = h
            lMax.append(curMax)
        curMax = 0
        for h in height[::-1]:
            if h > curMax:
                curMax = h
            rMax.append(curMax)
        rMax = rMax[::-1]
        res = 0
        for i, h in enumerate(height):
            if i<1 or i>=len(height)-1:
                continue
            # For given x-value, retrieve the left-maximum and right-maximum, which gives the depth of the local bowl
            # Subtract h to counter the effect of current block, and apply ReLU.
            res += max(0, min(lMax[i-1], rMax[i+1])-h)
        return res

"""
Time > 33.72%, Memory > 6.52%
Better, perhaps good enough.
"""