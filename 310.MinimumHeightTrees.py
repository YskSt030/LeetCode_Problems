import copy
class Solution:
    def findMinHeightTrees(self, n: int, edges):
        self.edges = edges
        ret = list()
        minval = -1
        for i in range(n):
            rval = self.culcdepth(i)
            if minval < 0:
                ret.append(i)
                minval = rval
            else:
                if minval > rval:
                    minval = rval
                    ret = list()
                    ret.append(i)
                elif minval == rval:
                    ret.append(i)
            
        return ret

    def culcdepth(self,n):
        edge = copy.deepcopy(self.edges)
        d = 0
        nodelist = dict()
        nodelist[d] = [n]
        num = n
        while len(edge) > 0:            
            if d not in nodelist.keys():
                break
            for num in nodelist[d]:
                edge_ = copy.deepcopy(edge)
                for e in edge:
                    if num in e:
                        val_ = e[0] if e[1] == num else e[1]                        
                        if d+1 not in nodelist.keys():
                            nodelist[d+1] = [val_]
                        else:
                            nodelist[d+1].append(val_)
                        edge_.remove(e)
                edge = copy.deepcopy(edge_)
            d += 1               
        return d
if __name__=='__main__':
    sol = Solution()
    n , edges = 1, []
    print(sol.findMinHeightTrees(n,edges))