"""
2023.05.22
"""
"""
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        vals = []
        def inorder(cur):
            if cur:
                inorder(cur.left)
                vals.append(cur.val)
                inorder(cur.right)
            else:
                vals.append(" ")
        inorder(root)
        for i in range(len(vals)//2):
            if vals[i]!=vals[len(vals)-i-1]:
                return False
        return True


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def levelorder(nodes):
            res = []
            vals = []
            if all([node is None for node in nodes]):
                return True
            for node in nodes:
                if node:
                    vals.append(node.val)
                    res.append(node.left)
                    res.append(node.right)
                else:
                    vals.append(" ")
            for i in range(len(vals) // 2):
                if vals[i] != vals[len(vals) - i - 1]:
                    return False
            return levelorder(res)

        return levelorder([root])

"""
Time > 9.2%, Memory > 32.4%
Runs okay, but slow and inefficient.
"""

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):

        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        return (left.val==right.val) and self.helper(left.left, right.right) and self.helper(left.right, right.left)

"""
Time > 24.22%, Memory > 11.83%
And/or operators can be super helpful.
Implement level order traversal without explicitly storing values and nodes in a level list.
"""