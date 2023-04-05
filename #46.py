"""
2023.04.05
"""
"""
46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(arr, cache=[]):
            if len(arr)==1:
                res.append(cache+arr)
                return
            for i in range(len(arr)):
                subarr = arr[:i]+arr[i+1:] if i < len(arr)-1 else arr[:i]
                subcache = cache + [arr[i]]
                helper(subarr, subcache)
        helper(nums)
        return res

"""
Time > 66.20%, Memory > 49.66%
Classic Dynamic Programming Example with no notable constraint.
"""