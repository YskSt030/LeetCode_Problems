"""
Given an array nums of n integers, are there elements a, b, c 
in nums such that a + b + c = 0? Find all unique triplets in the 
array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    #def threeSum(self, nums: List[int]) -> List[List[int]]:
    def threeSum(self, nums):
        ret = []
        posnums = [num for num in nums if num > 0]
        posnums.sort()
        negnums = [num for num in nums if num < 0]
        negnums.sort()
        iszero = 0 in nums
        if iszero:
            for num in posnums:
                if -num in negnums:
                    list_ = [-num,0,num]
                    if not list_ in ret:
                        ret.append(list_)
            if len([x for x in nums if x == 0]) >= 3:
                ret.append([0,0,0])

        for i in range(len(negnums) - 1):
            for j in range(i + 1, len(negnums)):
                val = negnums[i] + negnums[j]
                if -val in posnums:
                    list_ = [negnums[i] , negnums[j], -val]
                    if not list_ in ret:
                        ret.append(list_)
        for i in range(len(posnums) - 1):
            for j in range(i + 1, len(posnums)):
                val = posnums[i] + posnums[j]
                if -val in negnums:
                    list_ = [-val, posnums[i] , posnums[j]]
                    if not list_ in ret :
                        ret.append(list_)
        return ret

if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(nums))