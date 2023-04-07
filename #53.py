"""
2023.04.07
"""
"""
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""
class Solution:
    def maxSubArray(self, nums):
        # cumulative sum
        cumsum = nums[0]
        # Worst cumulative sum so far
        curmax = nums[0]
        # output
        res = curmax
        for i in range(1, len(nums)):
            cumsum += nums[i]
            # if curmax > 0, no need to subtract.
            res = max(res, max(cumsum-curmax, cumsum))
            # update current worst
            if curmax > cumsum:
                curmax = cumsum
        return res

"""
Time > 26.18%, Memory > 45.71%
Cumulatively add up elements, and subtract the smallest (if below zero) from the largest.
"""