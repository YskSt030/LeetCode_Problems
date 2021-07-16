"""
Given n non-negative integers representing an elevation map where 
the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped. 
Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

class Solution:
    #ef trap(self, height: List[int]) -> int:
    def trap(self, height) -> int:
        maxheight = max(height)
        ret = 0
        for h in range(1,maxheight + 1):
            start_point = 0
            end_point = len(height) - 1
            while height[start_point] < h:
                start_point += 1
            while height[end_point] < h:
                end_point -= 1
            print("start:{}, end:{}".format(start_point, end_point))
            if start_point == end_point:
                break
            print([a for a in height[start_point:end_point] if a < h])
            ret += len([a for a in height[start_point:end_point] if a < h])
        return ret

if __name__ == '__main__':
    sol = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(sol.trap(height))