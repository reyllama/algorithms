"""
2023.03.27
"""
"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def searchRange(self, nums, target):

        if len(nums) < 1:
            return [-1, -1]
        if len(nums) < 2:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        self.left, self.right = -1, -1

        def bisect(nums, target, l=None, r=None):
            print(l, r)
            if l == r:
                if nums[l] == target:
                    if l == 0:
                        self.left = l
                        self.right = max(self.right, l)
                    elif r == len(nums) - 1:
                        self.right = r
                        if self.left == -1:
                            self.left = r
                return
            if l > r:
                return
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid == 0:
                    self.left = mid
                elif nums[mid - 1] != target:
                    self.left = mid
                else:
                    bisect(nums, target, l=l, r=mid)
                if mid == len(nums) - 1:
                    self.right = mid
                elif nums[mid + 1] != target:
                    self.right = mid
                else:
                    bisect(nums, target, l=mid + 1, r=r)
            elif nums[mid] > target:
                bisect(nums, target, l=l, r=mid)
            else:
                bisect(nums, target, l=mid + 1, r=r)

        bisect(nums, target, 0, len(nums) - 1)

        return [self.left, self.right]

"""
Time > 53.7%, Memory: 5.38%
Working, but very messy. Looking for a cleaner code.
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Get the starting pos when target is present
        # Get The one in either boundary (of the chasm) when target is absent
        def search(x):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        lo = search(target)
        hi = search(target + 1) - 1

        if lo <= hi:
            return [lo, hi]

        return [-1, -1]

"""
Simply search for the 'lower bound (+1)' of the target range, by not specifying the condition when nums[mid]==x in search().
Then, we can get the higher bound by looking for a value slightly higher minus 1. Elegant.
"""