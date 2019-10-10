"""
Consider all the leaves of a binary tree.  From left to right order,
the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Note:

Both of the given trees will have between 1 and 100 nodes.

"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.leaf1 = []
        self.leaf2 = []
        self.getLeaf(root1, self.leaf1)
        self.getLeaf(root2, self.leaf2)
        return self.leaf1 == self.leaf2

    def getLeaf(self, root: TreeNode, leaf):
        if root and not root.left and not root.right:
            leaf.append(root.val)
        if root and root.left:
            self.getLeaf(root.left, leaf)
        if root and root.right:
            self.getLeaf(root.right, leaf)

if __name__ =='__main__':
    sol = Solution()

