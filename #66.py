"""
2023.04.12
"""
"""
66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        while digits[i]==9:
            digits[i]=0
            i -= 1
            if i == -1:
                return [1]+digits
        digits[i] += 1
        return digits

"""
Time > 45.36%, Memory > 93.43%
"""