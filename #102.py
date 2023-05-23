"""
2023.05.23
"""
"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        next_nodes = [root]
        while next_nodes:
            cur_nodes = next_nodes
            next_nodes = []
            level_vals = []
            for node in cur_nodes:
                level_vals.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            res.append(level_vals)
        return res

"""
Time > 18.77%, Memory > 18.3%
"""