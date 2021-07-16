"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numdict = dict()
        for num in nums:
            if num in list(numdict.keys()):
                numdict[num] = numdict[num] + 1
            else:
                numdict[num] = 1
        ret = [a for a in numdict.keys() if numdict[a] == 1]
        return ret[0]