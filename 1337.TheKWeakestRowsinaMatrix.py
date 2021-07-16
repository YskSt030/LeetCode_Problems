"""
Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), 
return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of 
soldiers in row j, or they have the same number of soldiers but i is less than j. 
Soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros.

Example 1:
Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 2 
row 1 -> 4 
row 2 -> 1 
row 3 -> 2 
row 4 -> 5 
Rows ordered from the weakest to the strongest are [2,0,3,1,4]

Example 2:
Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 1 
row 1 -> 4 
row 2 -> 1 
row 3 -> 1 
Rows ordered from the weakest to the strongest are [0,2,3,1]
 

Constraints:
m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.
"""

class Solution:
    #def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    def kWeakestRows(self, mat, k) :
        soldiernum_each_row = [[i,sum(mat[i])] for i in range(len(mat))]
        ret = []
        def sortnum(ret):
            num_index = ret[-1]
            num_val = soldiernum_each_row[ret[-1]][1]           
            while True:
                if num_index == 0:
                    break
                if num_val > soldiernum_each_row[num_index - 1][1]:
                    break
                if num_val < soldiernum_each_row[num_index - 1][1]:
                    ret[num_index],ret[num_index - 1] = ret[num_index -1],ret[num_index]
                elif num_val == soldiernum_each_row[num_index - 1][1] and ret[num_index] < ret[num_index - 1]:
                    ret[num_index],ret[num_index - 1] = ret[num_index -1],ret[num_index]                    
                num_index -= 1
            return ret
        for i in range(len(soldiernum_each_row)):
            ret.append(soldiernum_each_row[i][0])
            ret = sortnum(ret)
            if len(ret) > k:
                ret = ret[:-1]
        return ret
    def kWeakestRows2(self, mat, k):
        ret = sorted(range(len(mat)), key = lambda x: sum(mat[x])[:k]
        print(ret)

if __name__=='__main__':
    sol = Solution()
    mat =[[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
    k = 3
    print(sol.kWeakestRows2(mat, k))
        
        