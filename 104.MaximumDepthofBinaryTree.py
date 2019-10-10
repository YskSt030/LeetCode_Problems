"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    maxdep = 0
    def maxDepth(self, root: TreeNode) -> int:
        self.maxdep = 0
        if (root.val
