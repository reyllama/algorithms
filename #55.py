"""
2023.04.10
"""
"""
55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        jumpstones = [False] * len(nums)
        jumpstones[0] = True

        for i in range(len(nums)):
            if jumpstones[i]:
                jumpstones[i:i+nums[i]+1] = [True]*(nums[i]+1)
            else:
                return False
        return True

"""
Time > 5.1%, Memory > 6.22%
Slow and memory-consuming because of the list slicing.
"""

class Solution:
    def canJump(self, nums):
        maxidx = 0
        for i in range(len(nums)):
            if i > maxidx:
                return False
            maxidx = max(maxidx, i+nums[i])
        return True

"""
Time > 37.12%, Memory > 76.87%.
Note that we only need to keep how far we can get, not the intermediate availabilities.
"""