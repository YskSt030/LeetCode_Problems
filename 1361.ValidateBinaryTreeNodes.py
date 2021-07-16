
"""
You have n binary tree nodes numbered from 0 to n - 1 where 
node i has two children leftChild[i] and rightChild[i], 
return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

Example 1:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Example 2:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false

Example 3:
Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false

Example 4:
Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false
 
Constraints:
1 <= n <= 10^4
leftChild.length == rightChild.length == n
-1 <= leftChild[i], rightChild[i] <= n - 1

"""

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        nodes = list()
        for i in range(n):
            nodes.append(Node(i))
        used = [0]
        for i in range(n):
            if nodes[i].cleft == None and leftChild[i] != -1 and leftChild[i] not in used:
                nodes[i].cleft = nodes[leftChild[i]]
                used.append(leftChild[i])
            elif leftChild[i] != -1:
                return False
            if nodes[i].cright == None and rightChild[i] != -1 and rightChild[i] not in used:
                nodes[i].cright = nodes[rightChild[i]]
                used.append(rightChild[i])
            elif rightChild[i] != -1:
                return False
        for i in range(n):
            if i not in used:
                return False
        return True
            

class Node:
    def __init__(self, val_):
        self.val = val_
        self.cleft = None
        self.cright = None
    def setLeft(self, num):
        if num != -1:
            self.cleft = Node(num)
    def setRight(self, num):
        if num != -1:
            self.cright = Node(num)        
    