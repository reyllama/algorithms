"""
2023.04.14
"""
"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        from collections import Counter
        cnts = Counter(nums)
        nums[:cnts[0]]=[0]*cnts[0]
        nums[cnts[0]:cnts[0]+cnts[1]] = [1] * cnts[1]
        nums[cnts[0]+cnts[1]:cnts[0]+cnts[1]+cnts[2]] = [2] * cnts[2]

"""
Time > 75.72%, Memory > 50.53%
Naive solution, but works reasonably.
"""

class Solution:
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

"""
Reference answer, inspired from dutch partitioning problem.
"""