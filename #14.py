'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                ans += chars[0]
            else:
                break
        return ans

"""
Nothing to add. Better way to find out if we have identical cahracters, other than converting to a set?
"""
