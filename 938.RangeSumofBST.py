"""
Given the root node of a binary search tree,
return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.
Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23


Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.

"""

# Definition for a binary tree node.
# Binary tree: Parent >= left children, parent <= right children
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None




class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        node = TreeNode(root[0])
        for i in range(len(root)):
            self.insert(root[i])
        ret = 0
        temp_ = node
        while temp_.left != L:
            ret += temp_.left.val

    def insert(self, num, node: TreeNode):
        if num != None:
            if node.val < num:
                if node.right == None:
                    node.right = TreeNode(num)
                else:
                    node.insert(self.right)
            if node.val > num:
                if node.left == None:
                    node.left = TreeNode(num)
                else:
                    node.insert(node.left)




