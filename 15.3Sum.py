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
    def threeSum(self, nums):
               if len(nums) < 3:
            return []
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        else:
            nums.sort()
            ret = list()
            for i in range(len(nums)):
                p ,q = i + 1, len(nums) - 1
                tgt = -nums[i]
                if nums[i] == nums[i - 1]: continue
                while p < q:
                    if tgt > nums[p] + nums[q]:
                        p += 1                    
                    elif tgt < nums[p] + nums[q]:
                        q -= 1
                    else:
                        ret.append([nums[i], nums[p], nums[q]])
                        p += 1
                        q -= 1
            return ret
            
if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,-2,-1]
    print(sol.threeSum(nums))