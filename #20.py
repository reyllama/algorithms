"""
2023.03.17
"""

"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "}":"{", "]":"["}
        cache = []
        for par in s:
            if not pairs.get(par, False):
                cache.append(par)
            else:
                if len(cache)==0 or cache.pop() != pairs[par]:
                    return False
        return len(cache)==0

"""
Key idea: Whenever a closing bracket shows, the previous one has to be its pair. So we keep pop()-ing from 
the cache list of left brackets, to ensure everything closes in order. (and check their number balance)
Time > 91.75%, Memory > 59.78%
"""