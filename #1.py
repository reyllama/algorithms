"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compl = dict()
        for i, num in enumerate(nums):
            if compl.get(num, -1) >= 0:
                return [dict[num], i]
            compl[target-num] = i
        return False

"""
Naive하게 풀었다면 O(N^2) time complexity를 가졌을 문제인데, time complexity를 memory complexity로 바꿔서 linear time으로 해결하고자 하였다.
nums를 한번 enumerate하면서 이번 원소가 내가 찾던 원소인지를 dictionary를 통해 꺼내오도록 설계.
"""