"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        c1, c2 = (m+n-1)//2, (m+n)//2
        merged = []
        i, j = 0, 0
        while (i<m or j<n):
            n1, n2 = None, None
            if i<m:
                n1 = nums1[i]
            if j<n:
                n2 = nums2[j]
            if n1 and n2: # 둘 중 작은 값부터 append
                if n1 > n2:
                    merged.append(n2)
                    j += 1
                else:
                    merged.append(n1)
                    i += 1
            elif n1: # 남은 녀석을 append
                merged.append(n1)
                i += 1
            elif n2: # 남은 녀석을 append
                merged.append(n2)
                j += 1
            else:
                raise AssertionError
        return 0.5*(merged[c1]+merged[c2])

"""
두 개의 array를 효율적으로 merge 하기만 하면, 그 뒤엔 indexing으로 O(1)으로 찾을 수 있다.
"""