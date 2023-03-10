'''
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        nums = sorted(nums)
        for i, n in enumerate(nums[:-2]):
            l, r = i+1, len(nums)-1
            while l < r:
                offset = n + nums[l] + nums[r]
                if offset > 0:
                    r -= 1
                elif offset < 0:
                    l += 1
                else:
                    ans.append([n, nums[l], nums[r]])
                    l, r = l+1, r-1
        return ans


class Solution:
    # adjusting pointers while avoiding duplicates
    def adjust(self, nums, idx, dir):
        source = nums[idx]
        while nums[idx] == source:
            idx += dir
            if idx >= len(nums) or idx < 0:
                return idx
        return idx

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        nums = sorted(nums)
        # pivot pointer, starting from smallest to third largest (left-most number)
        p = 0
        while p < len(nums)-2:
            # We start from two extremes (min, max)
            l, r = p+1, len(nums)-1
            while l < r:
                offset = nums[p] + nums[l] + nums[r]
                # Make it smaller
                if offset > 0:
                    r -= 1
                # Make it larger
                elif offset < 0:
                    l += 1
                # Register answer and adjust pointers
                else:
                    ans.append([nums[p], nums[l], nums[r]])
                    l, r = self.adjust(nums, l, 1), self.adjust(nums, r, -1)
            # Adjust the pivot as well
            p = self.adjust(nums, p, 1)
        return ans

'''
Because we are keeping arrays, dropping duplicates can be tricky.
I am not sure if there is a more simple and efficient way, but I manually adjusted the pointers, 
so that no duplicate will be registered.
Note that when simply moving pointer by 1, duplicate can result when 1) the pivot is redundant and 2) both l+1 and r-1 don't change.
Time > 66.47%, Memory > 75.7%
'''