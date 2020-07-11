"""
Given a 2d grid map of '1's (land) and '0's (water), 
count the number of islands. An island is surrounded by water 
and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        if len(grid) > 0 and len(grid[0]) > 0:
            self.r = len(grid)
            self.c = len(grid[0])
            c_ = [0] * self.c
            self.area_counted = list()
            for j in range(self.r):
                self.area_counted.append(c_.copy())
            self.grid = grid
            for j in range(self.r):
                for i in range(self.c):
                    if self.grid[j][i] == '1' and self.area_counted[j][i] == 0:
                        ret += 1
                        self.searchArea(j,i)
        return ret                  
    
    def searchArea(self,j,i):
        if self.grid[j][i] == '1':
            self.area_counted[j][i] = 1
            if j > 0 and self.area_counted[j-1][i] == 0:
                self.searchArea(j-1,i)
            if j < self.r - 1 and self.area_counted[j + 1][i] == 0:
                self.searchArea(j + 1,i)
            if i > 0 and self.area_counted[j][i-1] == 0:
                self.searchArea(j,i-1)
            if i < self.c - 1 and self.area_counted[j][i + 1] == 0:
                self.searchArea(j,i + 1)       
