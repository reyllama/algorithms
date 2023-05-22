"""
2023.05.20
"""
"""
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(cur):
            if cur:
                helper(cur.left)
                res.append(cur.val)
                helper(cur.right)
            else:
                return None
        helper(root)
        return res

"""
Time > 24.79%, Memory > 7.26%
"""