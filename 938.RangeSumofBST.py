"""
Given the root node of a binary search tree, return the sum of values of
all nodes with value between L and R (inclusive).
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
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def insert(self,x):
        if x == null:
            pass
        elif self.val <= x:
            if self.right == None:
                self.right = TreeNode(x)
            else:
                self.insert(self.right)
        elif self.val > x:
            if self.left == None:
                self.left = TreeNode(x)
            else:
                self.insert(self.left)
    

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        ret = 0
        if root.val >= L and root.val <= R:
            ret += root.val
        
        if root.left :
            ret += self.rangeSumBST(root.left, L, R)
        if root.right :
            ret += self.rangeSumBST(root.right, L, R)
        return ret

if __name__ == '__main__':
    sol = Solution()
    root_list = [10,5,15,3,7,null,18]
    root = TreeNode(root_list[0])
    for i in range(1,len(root)):
        root.insert(root_list[i]) 
    L = 7
    R = 15
    print(sol.rangeSumBST(root, L, R))