"""

Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:


"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children



class Solution:
    def postorder(self, root: 'Node') -> List[int]:
