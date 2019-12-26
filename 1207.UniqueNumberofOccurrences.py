"""
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""



class Solution:
    #def uniqueOccurrences(self, arr: List[int]) -> bool:
    def uniqueOccurrences(self, arr) -> bool:
        index_ = []
        num_ = []
        for i in range(len(arr)):
            if len(index_) == 0 or arr[i] in index_ == False:
                index_.append(arr[i])
                num_.append(1)
            else:
                num[index_.index(arr[i])] += 1
        
                
def temp():
    a = [1,2,3,4,1,6,7]
    b = [7,6,5,4,3,2,1]
    c = a.index(1)
    d = b.index(1)
    exist = 8 in a
    debug = 1
      

if __name__ =='__main__':
    temp()
    sol = Solution()
    arr = [1,2,3,3,4,5,5,5,6,6,6,]
    print(sol.uniqueOccurrences(arr))