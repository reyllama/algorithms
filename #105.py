"""
2023.05.26
"""
"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.iidx = dict()
        self.p, self.i = preorder, inorder
        for i, v in enumerate(inorder):
            self.iidx[v] = i
        root = TreeNode(val=preorder[0])
        thresh = self.iidx[preorder[0]]
        left, right = preorder[1:thresh+1], preorder[thresh+1:]
        self.helper(root, left, right)
        return root

    def helper(self, cur, left, right):
        if left:
            cur.left = TreeNode(val=left[0])
            new_left, new_right = [], []
            if left[1:]:
                for node in left[1:]:
                    if self.iidx[node] < self.iidx[left[0]]:
                        new_left.append(node)
                    else:
                        new_right.append(node)
                self.helper(cur.left, new_left, new_right)
        if right:
            cur.right = TreeNode(val=right[0])
            new_left, new_right = [], []
            if right[1:]:
                for node in right[1:]:
                    if self.iidx[node] < self.iidx[right[0]]:
                        new_left.append(node)
                    else:
                        new_right.append(node)
                self.helper(cur.right, new_left, new_right)

"""
Time > 5.1%, Memory > 52.7%
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
      if not preorder or not inorder:
        return None
      root = TreeNode(preorder[0])
      mid = inorder.index(preorder[0])
      root.left = self.buildTree(preorder[1 : mid + 1],inorder[:mid])
      root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
      return root

"""
Time > 16.41%, Memory > 12.30%
"""