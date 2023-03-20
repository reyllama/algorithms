"""
2023.03.20
"""
"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l, r = n, n
        ans =[]

        def generator(l=n, r=n, cache=""):
            if l:
                generator(l-1, r, cache+"(")
            if l<r:
                generator(l, r-1, cache+")")
            if not r:
                ans.append(cache)
        generator()
        return ans

"""
Time > 97.14%, Memory > 29.54%
Simple Exhaustive Search using DP.
"""