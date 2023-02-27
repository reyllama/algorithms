"""
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            cursum = numbers[i] + numbers[j]
            if cursum == target:
                return [i+1, j+1] # 1-indexed
            elif cursum < target:
                i += 1
            else:
                j -= 1
        return

"""
Sorted가 되어있다는 구조를 잘 활용하는 것이 핵심. 대신 extra memory에 의존하지 않는 답안을 제시해야 한다.
이 세팅에서는 최솟값과 최댓값에서 시작하는 두 개의 커서를 운용하면, 각 커서를 어느 방향으로 움직여야 할지를 확정할 수 있다.
cache를 쌓아가는 대신 cursor를 움직이는 직관이 중요한 것 같다.
"""