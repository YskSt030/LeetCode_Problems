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
        if len(nums) <= 3:
            return 0
    
    def insertionSort(arr): 
        for i in range(1, len(arr)): 
            key = arr[i] 
            j = i-1
            while j >=0 and key < arr[j] : 
                    arr[j+1] = arr[j] 
                    j -= 1
            arr[j+1] = key 
                


if __name__ == '__main__':
    sol = Solution()
    numl = [2, 4, 7, 3, 5, 9, 0]
    sol.sort(numl)
    print(numl)
            


        