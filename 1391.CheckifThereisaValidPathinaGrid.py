"""
Given a m x n grid. Each cell of the grid represents a street. The street of grid[i][j] can be:
1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.

"""

class Solution:
    #def hasValidPath(self, grid: List[List[int]]) -> bool:
    def hasValidPath(self, grid) -> bool:   
        already_passed = list()
        x = 0
        y = 0
        self.retnum = 0
        ret = self.findroute(x, y, grid,already_passed)
        if self.retnum > 0:
            return True
        else:
            return False

    def findroute(self, x, y, grid, already_passed):
        M = len(grid)
        N = len(grid[0])
        
        if x == M - 1 and y == N - 1:
            self.retnum += 1
            return True
        if x >= N or x < 0 or y >= M or y < 0:
            return False
        
        if (grid[y][x] == 1 or grid[y][x] == 3 or grid[y][x] == 5 ) and not [y, x - 1] in already_passed:
            already_passed.append([y,x])
            self.findroute(x - 1, y, grid, already_passed)
        if (grid[y][x] == 1 or grid[y][x] == 4 or grid[y][x] == 6 ) and not [y, x + 1] in already_passed:
            already_passed.append([y,x])
            self.findroute( x + 1, y, grid, already_passed)
        if (grid[y][x] == 2 or grid[y][x] == 5 or grid[y][x] == 6 ) and not [y - 1, x] in already_passed:
            already_passed.append([y,x])
            self.findroute( x , y - 1, grid, already_passed)
        if (grid[y][x] == 2 or grid[y][x] == 3 or grid[y][x] == 4 ) and not [y + 1, x] in already_passed:
            already_passed.append([y,x])
            self.findroute(x , y + 1, grid, already_passed)
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    grids =[ [[2,4,3],[6,5,2]],[[1,2,1],[1,2,1]], [[1,1,2]], [[1,1,1,1,1,1,3]], [[2],[2],[2],[2],[2],[2],[6]]]
    
    for grid in grids:
        print(sol.hasValidPath(grid))