"""
2023.03.31
"""
"""
41. First Missing Positive

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        lohi, hilo = dict(), dict()

        for n in nums:
            if n < 1 or lohi.get(n, False):
                continue
            if lohi.get(n+1, False) and hilo.get(n-1, False):
                lohi[hilo[n-1]] = lohi[n+1]
                hilo[lohi[n+1]] = hilo[n-1]
            elif lohi.get(n+1, False):
                hilo[lohi[n+1]] = n
            elif hilo.get(n-1, False):
                lohi[hilo[n-1]] = n
            lohi[n] = lohi.get(n+1, n)
            hilo[n] = hilo.get(n-1, n)

        return lohi.get(1, 0) + 1

"""
Time > 5%, Memory > 5%
Not a satisfactory solution that uses A LOT of extra space.
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        N = len(nums)
        for i in range(N):
            if nums[i]<1 or nums[i]>=N:
                nums[i] = 0
        for i in range(N):
            nums[nums[i]%N] += N
        print(nums)
        for i in range(1, N):
            if nums[i] // N == 0:
                return i
        return N
"""
Time > 18.34%, Memory > 50.29%
Key idea: 'Alter the given array IN-PLACE to restrain from using EXTRA MEMORY'
Fix len(nums) as the pivot, and operate on modulus to change array values in-place.
"""