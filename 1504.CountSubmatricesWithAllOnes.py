"""
Given a rows * columns matrix mat of ones and zeros, 
return how many submatrices have all ones.

Example 1:
Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.

Example 2:
Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.

Example 3:
Input: mat = [[1,1,1,1,1,1]]
Output: 21

Example 4:
Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
Output: 5
 
Constraints:

1 <= rows <= 150
1 <= columns <= 150
0 <= mat[i][j] <= 1
"""
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if len(mat) < 1:
            return 0
        self.ret = 0
        self.mat = mat
        self.R = len(mat)
        self.C = len(mat[0])
        for x in range(self.C):
            for y in range(self.R):
                if mat[y][x] == 1:
                    self.find(x,y)
        return self.ret

    def find(self,x,y):
        i = 0
        minc = 151
        while True:
            if x + i >= self.C:
                break
            elif self.mat[y][x + i] == 0:
                break
            else:
                j = 1
                self.ret += 1
                while j < minc:
                    if y + j >= self.R:
                        if minc > j:
                            minc = j
                        break
                    if self.mat[y + j][x + i] == 1:
                        self.ret += 1
                    else:
                        if minc > j:
                            minc = j
                        break
                    j += 1
            i += 1