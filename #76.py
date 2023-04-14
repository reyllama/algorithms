"""
2023.04.14
"""
"""
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def entail(cnt_A, cnt_B):
            for k in cnt_B.keys():
                if cnt_A.get(k, 0) < cnt_B[k]:
                    return False
            return True

        from collections import Counter
        base = Counter(s)
        target = Counter(t)
        if not entail(base, target):
            return ""
        res = s
        for i in range(len(s)-len(t)+1):
            j = len(s)
            base = Counter(s[i:j])
            while entail(base, target):
                if len(s[i:j]) < len(res):
                    res = s[i:j]
                j -= 1
                base[s[j]] -= 1
        return res

"""
Time Limit Exceeded. (264/267)
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N = len(t)
        if len(s) < N:
            return ""

        from collections import defaultdict

        def entail(cnt_A, cnt_B):
            for k in cnt_B.keys():
                if cnt_A.get(k, 0) < cnt_B[k]:
                    return False
            return True

        def counter(arr):
            cnt = defaultdict(int)
            for a in arr:
                cnt[a] += 1
            return cnt

        target = counter(t)

        for w in range(N, len(s)+1):
            base = counter(s[:w])
            if entail(base, target):
                return s[:w]
            for i in range(1, len(s)-w+1):
                base[s[i-1]] -= 1
                base[s[w+i-1]] += 1
                if entail(base, target):
                    return s[i:i+w]

        return ""

"""
Time Limit Exceeded. (265/267)
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        base, target = Counter(), Counter(t)
        l, r, shortest = 0, 0, len(s)+1
        res_l, res_r = l, r
        if len(s) < len(t):
            return ""
        while r < len(s):
            base[s[r]] += 1
            while l<=r and all([base[c]>=target[c] for c in target]):
                if r-l+1 < shortest:
                    shortest = r-l+1
                    res_l, res_r = l, r
                base[s[l]] -= 1
                l += 1
            r += 1
        return s[res_l:res_r+1] if shortest <= len(s) else ""

"""
Time > 5.1%, Memory > 72.35%
Maximally exploit the previous state by dynamically changing left and right index.
Also, note for all() function that comes in handy.
"""