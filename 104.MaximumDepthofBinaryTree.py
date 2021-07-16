"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return self.findchildren(root,1)
          
    def findchildren(self,node, num):
        ret_l = num
        ret_r = num
        if node.left !=None:
            ret_l = self.findchildren(node.left, num + 1)
        if node.right !=None:
            ret_r = self.findchildren(node.right, num + 1)
        
        return max(num, ret_l, ret_r)