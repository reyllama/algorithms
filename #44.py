"""
2023.04.04
"""
"""
44. Wildcard Matching

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pt = ""
        for i in range(len(p)):
            if p[i] != "*":
                pt += p[i]
            else:
                if not pt or pt[-1] != "*":
                    pt += p[i]
        p = pt
        res = False
        i, j = 0, 0
        w = p.count("*")
        while j < len(p):
            char = p[j]
            if i >= len(s) and char != "*":
                return False
            if char == "?":
                i, j = i+1, j+1
            elif char == "*":
                for k in range(len(s[i:])-len(p[j:])+w+1):
                    print(i,j,k)
                    res = self.isMatch(s[i+k:], p[j+1:])
                    if res:
                        return res
                return False
            else:
                if s[i]==p[j]:
                    i, j = i+1, j+1
                else:
                    res = False
                    break
        if i == len(s):
            return True
        return res

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pt = p.replace("*", "").replace("?", "")
        st = s[:]
        for char in pt:
            exis = False
            for i, n in enumerate(st):
                print(n, char)
                if char == n:
                    st = st[i+1:]
                    exis = True
                    break
            if not exis:
                return exis
        pt = ""
        for i in range(len(p)):
            if p[i] != "*":
                pt += p[i]
            else:
                if not pt or pt[-1] != "*":
                    pt += p[i]
        p = pt
        print(s, p)
        res = False
        i, j = 0, 0
        w = p.count("*")
        while j < len(p):
            char = p[j]
            if i >= len(s) and char != "*":
                return False
            if char == "?":
                i, j = i+1, j+1
            elif char == "*":
                for k in range(len(s[i:])-len(p[j:])+w+1):
                    print(i,j,k)
                    res = self.isMatch(s[i+k:], p[j+1:])
                    if res:
                        return res
                return False
            else:
                if s[i]==p[j]:
                    i, j = i+1, j+1
                else:
                    res = False
                    break
        if i == len(s):
            return True
        return res

class Solution:
    def check(self, seg, chars):
        corr = True
        for x, y in zip(seg, chars):
            if x == "?":
                continue
            if x != y:
                corr = False
                break
        return corr

    def isMatch(self, s: str, p: str) -> bool:
        # Remove consecutive asterisks
        pt = ""
        for i in range(len(p)):
            if p[i] != "*":
                pt += p[i]
            else:
                if not pt or pt[-1] != "*":
                    pt += p[i]
        segs = pt.split("*")
        if len(segs)==1:
            if len(s)!=len(p):
                return False
        print("A")
        if segs[0] != "":
            if not self.check(segs[0], s[:len(segs[0])]):
                return False
        print("B")
        if segs[-1] != "":
            if not self.check(segs[-1], s[-len(segs[-1]):]):
                return False
        print("C")
        for seg in segs:
            exis = False
            for i in range(len(s)-len(seg)+1):
                chars = s[i:i+len(seg)]
                print(seg, chars)
                corr = True
                for x, y in zip(seg, chars):
                    if x == "?":
                        continue
                    if x != y:
                        corr = False
                        break
                if corr:
                    exis = True
                    s = s[i+len(seg):]
                    break
            if not exis:
                return exis
        return True

"""
Time > 87.8%, Memory > 87.59%
1/ Replace consecutive * (because they are meaningless when more than 1 in a row)
2/ Split the pattern by * (to obtain chunks that should appear CONSECUTIVELY)
3/ When the split output is length 1, it means that there are no * in the pattern, hence the length should match
4/ If the pattern doesn't start or end with *, then the corresponding pre/suf-fix should match
5/ For each chunk splitted by *, see if they exist in s, and cut the leading part off for searching the next chunk.
(We can greedily cut off the heads because the earliest cutoff contains other cases) 
"""