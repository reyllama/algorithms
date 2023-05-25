"""
2023.05.25
"""
"""
103. Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        next_nodes = [root]
        tik = 0
        while next_nodes:
            cur_nodes = next_nodes
            cur_vals = []
            next_nodes = []
            for node in cur_nodes:
                if node:
                    cur_vals.append(node.val)
                    next_nodes.append(node.left)
                    next_nodes.append(node.right)
            if tik:
                cur_vals = cur_vals[::-1]
            tik = 1-tik
            if cur_vals:
                res.append(cur_vals)
        return res

"""
Time > 20.33%, Memory > 7.83%
"""