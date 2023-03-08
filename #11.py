"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

from collections import defaultdict

class Solution:
    def maxArea(self, height: List[int]) -> int:
        hash = defaultdict(list)
        # Organize height into dict for faster retrieval in O(n)
        for i, h in enumerate(height):
            hash[h].append(i)
        # From highest to lowest
        sorted_keys = sorted(list(hash.keys()))
        # Left/Right-most point so far (current height or higher)
        lmost, rmost = len(height), 0
        curMax = 0
        while sorted_keys:
            # Start from highest value
            h = sorted_keys.pop()
            # It's no use checking lower points as it cannot overtake curMax
            if curMax >= h*(len(height)-1):
                break
            # Update peripheries if necessary
            rmost = max(hash[h][-1], rmost)
            lmost = min(hash[h][0], lmost)
            curMax = max(curMax, h*(rmost - lmost))
        return curMax

'''
Horizontal traversing inevitably results in inefficiencies.
Instead, start from the highest poles and gradually lower the bar.
Keeping track only of the leftmost and rightmost pole is also an important idea.
Time > 96.32%, Memory > 97.53%
'''