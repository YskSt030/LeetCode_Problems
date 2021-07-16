"""
Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and 
verticalCuts where horizontalCuts[i] is the distance from the top of the rectangular cake to the 
ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular 
cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position 
provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, 
return this modulo 10^9 + 7.

 

Example 1:
Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. 
Red lines are the horizontal and vertical cuts. After you cut the cake, 
the green piece of cake has the maximum area.

Example 2:
Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. 
Red lines are the horizontal and vertical cuts. After you cut the cake, 
the green and yellow pieces of cake have the maximum area.

Example 3:
Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
 
Constraints:

2 <= h, w <= 10^9
1 <= horizontalCuts.length < min(h, 10^5)
1 <= verticalCuts.length < min(w, 10^5)
1 <= horizontalCuts[i] < h
1 <= verticalCuts[i] < w
It is guaranteed that all elements in horizontalCuts are distinct.
It is guaranteed that all elements in verticalCuts are distinct.
"""
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hc,vc = horizontalCuts,verticalCuts
        hc.sort()
        vc.sort()
        reth ,retv = hc[0],vc[0]
        MOD = 1000000007
        if len(hc) > 1:
            for i in range(1,len(hc)):
                tmp = hc[i] - hc[i-1]
                if tmp > reth:
                    reth = tmp
        reth = max(reth, h - hc[-1])
        if len(vc) > 1:
            for i in range(1,len(vc)):
                tmp = vc[i] - vc[i-1]
                if tmp > retv:
                    retv = tmp
        retv = max(retv, w - vc[-1])
        return (reth * retv) % MOD