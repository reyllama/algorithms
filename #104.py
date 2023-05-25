"""
2023.05.25
"""
"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        next_nodes = [root]
        while next_nodes:
            cur_nodes = next_nodes
            next_nodes = []
            for node in cur_nodes:
                if node:
                    next_nodes.append(node.left)
                    next_nodes.append(node.right)
            if next_nodes:
                res += 1
        return res

"""
Time > 36.88%, Memory > 45.90%
"""