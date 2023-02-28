"""
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))

        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                res[i+j] += int(n1) * int(n2)
                res[i+j+1] += res[i+j] // 10 # carry
                res[i+j] = res[i+j] % 10

        while len(res) > 1 and res[-1] == 0: # answer can be sheer '0'
            res.pop()

        return "".join([str(x) for x in res[::-1]])