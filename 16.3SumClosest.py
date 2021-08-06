"""
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that 
each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    #def threeSumClosest(self, nums: List[int], target: int) -> int:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        if target<nums[0] * 3:
            return sum(nums[:3])
        elif target > nums[-1] * 3:
            return sum(nums[-3:])
        N = len(nums)
        ret = 10**6
        flag = False
        def find(l,tgt):
            p,q = 0, len(l)-1
            while p+1<q:
                m = (p+q)//2
                if l[m] < tgt:
                    p = m
                else:
                    q = m
            return l[p] if tgt-l[p] <=l[q] -  tgt else l[q]
        for i in range(N-2):
            #if flag:
            #    break
            for j in range(i+1,N-1):
                #if ret < nums[i] + nums[j]:
                #    flag = True
                #    break
                tmp = target - (nums[i] + nums[j])
                k = find(nums[j+1:],tmp)
                if target - (nums[i]+nums[j]+k) == 0:
                    return target
                if abs(target - (nums[i]+nums[j]+k)) < abs(target - ret):
                    ret = nums[i]+nums[j]+k
        return ret
                

if __name__ == '__main__':
    sol = Solution()
    numl = [-1,2,1,-4]
    tgt = 1
    print(sol.threeSumClosest(numl,tgt))
            


        