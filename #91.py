"""
2023.05.17
"""
"""
91. Decode Ways

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        self.res = 0
        def helper(sub):
            if len(sub)==0:
                self.res += 1
                return
            if sub[0]=='0':
                return
            if len(sub)>1 and sub[0]=="1":
                helper(sub[1:]) or helper(sub[2:])
            elif len(sub)>1 and sub[0]=='2':
                if sub[1] in '0123456':
                    helper(sub[1:]) or helper(sub[2:])
                else:
                    helper(sub[1:])
            else:
                helper(sub[1:])
        helper(s)
        return self.res

"Time Limit Exceeded"

class Solution:
    def numDecodings(self, s: str) -> int:
        res = 1
        end = 0
        for i, c in enumerate(s):
            if c == '0':
                if end == 0:
                    return 0
                if i > 1 and s[i-2] in [1,2]:
                    res -= 1
                end = 0
            elif c in '12':
                if end in [1,2]:
                    res += 1
                end = int(c)
            elif c in '3456':
                if end in [1,2]:
                    res += 1
                end = 0
            else:
                if end == 1:
                    res += 1
                end = 0
        return res

"Wrong Answer. Because we consider not only the previous state but the state before that dynamically." \
"For example, consider the case, [1123]. With the last 3, we have to add 2 not 1."

class Solution:
    def numDecodings(self, s: str) -> int:
        res = [1]
        end = '0'
        for i, c in enumerate(s):
            if c == '0':
                if end not in '12':
                    return 0
                res.append(res[-2])
            elif c in '123456':
                if end in '12':
                    res.append(res[-1]+res[-2])
                else:
                    res.append(res[-1])
            else:
                if end == '1':
                    res.append(res[-1]+res[-2])
                else:
                    res.append(res[-1])
            end = c
        return res[-1]

"""
Time > 31.1%, Memory > 24.71%
<Idea> 
When 0 shows up, it HAS TO combine with leading 1 or 2, otherwise the sequence is impossible.
When 123456 show up and the previous digit was 1 or 2, it can either (1) combine or (2) stand alone. 
This case, we have to add the two previous states, because both cases are plausible to end with current digit.
When 789 show up, only when previous digit was 1 we add two prev states.
Otherwise, the number of cases is unchanged from the previous state, as it HAS TO stand alone.
"""