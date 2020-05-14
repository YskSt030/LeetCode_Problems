"""
Given n non-negative integers a1, a2, ..., an , where each 
represents a point at coordinate (i, ai). n vertical lines are 
drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that 
the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        ret = 0
        while r > l:
            ret = max(ret, min(height[l],height[r]) *(r-l))

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return ret
        

if __name__ == '__main__':
    sol = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    ret = sol.maxArea(height)
