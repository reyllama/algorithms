"""
2023.05.20
"""
"""
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        def helper(cur):
            if cur:
                helper(cur.left)
                res.append(cur.val)
                helper(cur.right)
            else:
                return
        helper(root)
        for i, r in enumerate(res[1:]):
            if r <= res[i]:
                return False
        return True

"""
Time > 45.52%, Memory > 7.31%
Idea: Unroll BST by in-order traversal and check if the resulting value array is sorted in ascending order.
"""