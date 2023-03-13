"""
2023. 03. 13
"""
"""
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""

class Solution:
    def adjust(self, nums, idx, dir, lt, rt):
        src = nums[idx]
        while nums[idx] == src:
            idx += dir
            if idx < lt or idx > rt:
                return idx
        return idx

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        le, re = 0, len(nums)-1
        ans = []
        while le < re:
            offset = target-(nums[le]+nums[re])
            li, ri = le+1, re-1
            while li < ri:
                if nums[li]+nums[ri]>offset:
                    ri = self.adjust(nums, ri, -1, li, ri)
                elif nums[li]+nums[ri]<offset:
                    li = self.adjust(nums, li, 1, li, ri)
                else:
                    ans.append([nums[le], nums[li], nums[ri], nums[re]])
                    li = self.adjust(nums, li, 1, li, ri)
                    ri = self.adjust(nums, ri, -1, li, ri)
            le = self.adjust(nums, le, 1, le, re)
            re = self.adjust(nums, re, -1, le, re)
        return ans

"""
양 끝점을 움직이는 포인트들을 모두 거쳐야하므로 재귀호출을 이용해서 구현하는 게 더 나을 것 같다.
"""

class Solution:
    def adjust(self, nums, idx, dir):
        source = nums[idx]
        while nums[idx] == source:
            idx += dir
            if idx >= len(nums) or idx < 0:
                return idx
        return idx
    def threeSum(self, nums, target):
        ans = list()
        p = 0
        while p < len(nums)-2:
            l, r = p+1, len(nums)-1
            while l < r:
                offset = nums[p] + nums[l] + nums[r]
                if offset > target:
                    r -= 1
                elif offset < target:
                    l += 1
                else:
                    ans.append([nums[p], nums[l], nums[r]])
                    l, r = self.adjust(nums, l, 1), self.adjust(nums, r, -1)
            p = self.adjust(nums, p, 1)
        return ans
    def fourSum(self, nums, target):
        out = []
        nums = sorted(nums)
        i = 0
        while i < len(nums)-3:
            ret = self.threeSum(nums[i+1:], target-nums[i])
            out += [[nums[i]]+arr for arr in ret]
            print(i, out)
            i = self.adjust(nums, i, 1)
        return out

"""
ThreeSum을 그대로 활용해서, 가장 왼쪽 피봇을 오른쪽으로 밀어가면서 exhaustive search.
Time > 71%, Memory > 88.11%
"""

class Solution:
    def fourSum(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results

"""
This recursive implementation generalizes to N-sum.
"""