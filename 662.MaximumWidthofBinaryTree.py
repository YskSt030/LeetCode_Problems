"""
Given a binary tree, write a function to get the maximum width of the given tree. 
The width of a tree is the maximum width among all levels. The binary tree has 
the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes 
(the leftmost and right most non-null nodes in the level, where the null nodes 
between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 
(6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.D = defaultdict(list)
        node = root
        self.search(node, 1, 0)
        ret = 0
        for c in self.D.keys():
            ret = max(max(self.D[c]) - min(self.D[c]), ret)
        return ret + 1
    def search(self, node, num, depth):
        if node != None:
            self.D[depth].append(num)
            self.search(node.left, num * 2, depth + 1)
            self.search(node.right, num * 2 + 1, depth + 1)
            