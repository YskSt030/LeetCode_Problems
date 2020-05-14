"""
Given an array arr, replace every element in that array with the greatest element 
among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) < 1:
            return [-1]
        else:
            ret = [-1] * len(arr) 
            for i in range(len(arr) - 2, -1, -1):
                ret[i] = max(ret[i+1], arr[i+1])

        return ret