class Solution:
    def maxDistance(self, arrays) -> int:
        maxl = list()
        minl = list()
        if len(arrays) == 0:
            return 0
        for i in range(len(arrays)):
            maxl.append([i,arrays[i][-1]]) 
            minl.append([i,arrays[i][0]]) 
        maxl.sort(key=lambda x:x[1],reverse=True)
        minl.sort(key=lambda x:x[1])
        if minl[0][0] != maxl[0][0]:
            return maxl[0][1] - minl[0][1]
        else:
            return max(maxl[0][1] - minl[1][1],maxl[1][1] - minl[0][1])
            

if __name__=='__main__':
    sol = Solution()
    arrays = [[1,5],[3,4]]
    print(sol.maxDistance(arrays))