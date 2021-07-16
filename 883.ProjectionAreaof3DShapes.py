"""
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
Now we view the projection of these cubes onto the xy, yz, and zx planes.
A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.
Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
Return the total area of all three projections.

"""


class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        ret = 0
        X = len(grid)
        Y = len(grid[0])
        for i in range(X):
            ret = ret + max(grid[i])  # Y axis
        for j in range(Y):
            max_y = 0
            for i in range(X):
                if grid[i][j] > 0:
                    ret = ret + 1  # Z axis
                if max_y < grid[i][j]:
                    max_y = grid[i][j]
            ret = ret + max_y  # X axis
        return ret
