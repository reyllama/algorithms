"""
2023.03.21
"""
"""
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, n = 0, len(needle)
        while i+n <= len(haystack):
            if haystack[i:i+n] == needle:
                return i
            i += 1
        return -1

""" 
Time > 89.58%, Memory > 95.11%
"""

