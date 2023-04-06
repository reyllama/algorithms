"""
2023.04.06
"""
"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        cache = defaultdict(list)
        for st in strs:
            sst = "".join(sorted(st))
            cache[sst].append(st)
        return [v for v in cache.values()]

"""
Time > 87.48%, Memory > 82.72%
Sort once, and use this sorted version as the key for each anagram group.
"""