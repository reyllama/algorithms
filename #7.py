'''
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        2147483648
        8463847412
        """
        pos = x>0
        lim = [214748364, 7 if pos else 8]
        x = abs(x)
        ans = 0

        while x != 0:
            digit = x % 10
            x //= 10

            if ans > lim[0] or (ans==lim[0] and digit>lim[1]):
                return 0

            ans = ans*10 + digit

        return ans if pos else -ans

"""
환경의 제약 상 32 bit integer를 초과하는 숫자를 할당하면 overflow가 발생하는 상황이므로, reversed output을 digit 단위로 단계적으로 쌓아나가면서
넘치기 직전에 스탑을 해야한다.
"""