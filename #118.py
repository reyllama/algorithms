"""
2023.06.02
"""
"""
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            cur, prev = [1], res[-1]
            for i in range(len(prev)-1):
                cur.append(prev[i]+prev[i+1])
            cur.append(1)
            res.append(cur)
        return res

"""
Time > 30.22%, Memory > 16.60%
"""