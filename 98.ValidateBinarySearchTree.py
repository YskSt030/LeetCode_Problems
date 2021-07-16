class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.ret = True
        def dfs(node):
            
            if self.ret == True:
                if node.left != None:
                    if node.left.val > node.val:
                        ret =  False
                    else:
                        ret = dfs(node.left)
                if node.right != None:
                    if node.right.val < node.val:
                        ret = False
                    else:
                        ret = dfs(node.left)
        dfs(root) 
        return ret

if __name__=='__main__':
    sol = Solution()
