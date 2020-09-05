"""
Given two binary search trees root1 and root2.
Return a list containing all the integers from both trees sorted in ascending order.

Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:
Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:
Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

Example 5:
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]

Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        node1,node2 = root1,root2
        list1,list2 = list(),list()
        def printnode(node, list_):
            if node!= None:
                if node.left!=None:
                    printnode(node.left, list_)          
                list_.append(node.val)
                if node.right!= None:
                    printnode(node.right, list_)

        printnode(node1,list1)
        printnode(node2,list2)


        if len(list1) == 0 and len(list2) == 0:
            return []
        elif len(list1) == 0 and len(list2) > 0:
            return list2
        elif len(list2) == 0 and len(list1) > 0:
            return list1
        else:
            ret = list()
            p,q = 0,0
            while True:

                if list1[p] < list2[q]:
                    ret.append(list1[p])
                    p += 1              
                elif list1[p] > list2[q]:
                    ret.append(list2[q])
                    q += 1
                else:
                    ret.append(list1[p])
                    ret.append(list2[q])
                    p,q = p + 1, q + 1
                if p == len(list1) and q < len(list2):
                    ret.extend(list2[q:])
                    break
                if q == len(list2) and p < len(list1):
                    ret.extend(list1[p:])
                    break
                if q == len(list2) and p == len(list1):
                    break
            return ret