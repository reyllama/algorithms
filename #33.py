"""
2023.03.24
"""
"""
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

# O(log n) constraint calls for bisection.
class Solution:
    def bisection(self, nums, target, l, r):
        # l: leftmost index
        # r: rightmost index (len(nums)-1 format, in other words, inclusive)
        while l<r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid+1
        if l==r and nums[l]==target:
            return l
        return -1

    def search(self, nums, target, left=None, right=None):
        # At Initialization
        if left is None:
            left = 0
        if right is None:
            right = len(nums)-1
        # Edge Case
        if left==right:
            return left if nums[left]==target else -1
        mid = (left+right)//2
        if nums[mid]==target:
            return mid
        # left array is sorted and contains target
        if left<=mid-1 and nums[left]<=target and target<=nums[mid-1]:
            return self.bisection(nums, target, left, mid-1)
        # right array is sorted and contains target
        if mid+1 <= right and nums[mid+1] <= target and target <= nums[right]:
            return self.bisection(nums, target, mid+1, right)
        # left array is not sorted -> recursively apply search() function
        if left <= mid-1 and nums[left] > nums[mid-1]:
            return self.search(nums, target, left, mid-1)
        # right array is not sorted -> recursively apply search() function
        elif mid+1 <= right and nums[mid+1] > nums[right]:
            return self.search(nums, target, mid+1, right)
        # no clear solution + both sides are sorted -> no more place to look
        else:
            return -1

"""
Time > 51.12%, Memory > 12.1%
Tricky Question where I have to be really careful about the boundary conditions. (Literal boundaries, short array inputs)
Idea: We recursively take midpoints (bisect) to decompose the array into sorted arrays, and once we have a sorted array
that contains the target within its boundary, once again apply bisection to find out the index.
Writing code that works and reads is more important, than writing code that is concise and elegant.
"""