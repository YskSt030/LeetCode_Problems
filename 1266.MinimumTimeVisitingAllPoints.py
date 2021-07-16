"""
On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time_taken = 0
        for i in range(len(points)-1):
            dx, dy = points[i][0] - points[i+1][0],points[i][1] - points[i+1][1]
            if dx < 0:
                dx = -dx
            if dy < 0:
                dy = -dy
            if dy >= dx:
                time_taken += dy
            else:
                time_taken += dx
        return time_taken