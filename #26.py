"""
2023.03.21
"""
"""
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i]==nums[i+1]:
                del nums[i+1]
            else:
                i += 1
        return len(nums)

"""
Time > 21.25%, Memory > 51.16%
How come others are faster than this?
Maybe del operation is slow in python.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i]==nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1
        return len(nums)

"""
Time > 20.21%, Memory > 51.16%
No gain from switching to pop().
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in range(1, len(nums)):
            if nums[i]!=nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1

"""
Time > 74.92%, Memory > 51.16%
For this problem in specific, we don't need to actually remove any element.
We just have to alter the first k elements so that nums[:k] correspond to the unique values.
This simple assignment makes the operation faster, as we don't interfere the entire memory structure.
"""