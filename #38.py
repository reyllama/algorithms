"""
2023.03.31
"""
"""
38. Count and Say

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.
"""
class Solution:
    def say(self, arr):
        cur, cnt, out = arr[0], 1, ""
        for i in range(1, len(arr)):
            if arr[i] != cur:
                out += f"{cnt}{cur}"
                cur, cnt = arr[i], 1
            else:
                cnt += 1
        out += f"{cnt}{cur}"
        return out

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.say(self.countAndSay(n-1))

"""
Time > 92.2%, Memory > 78.68%
Very intuitive, easy.
"""