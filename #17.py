"""
2023. 03. 13
"""
"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""


class Solution:
    def product(self, arr, chars):
        out = []
        for c in chars:
            out += [a + c for a in arr]
        return out

    def letterCombinations(self, digits: str) -> List[str]:
        maps = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans = ['']

        if len(digits) == 0:
            return []

        for i, d in enumerate(digits):
            ans = self.product(ans, maps[d])
            print(i, d, ans)

        return ans

"""
Efficiently expanding the cache array is the key. 3-fold for-loop is inevitable.
Time > 82.1%, Memory > 67.71%
"""