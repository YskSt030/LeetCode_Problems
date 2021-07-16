"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, 
return a sorted array of only the integers that appeared in all three arrays.

Example 1:
Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
 

Constraints:
1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""

class Solution:
    #def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    def arraysIntersection(self, arr1, arr2, arr3):
        return [x for x in set(arr1 + arr2 + arr3) if (arr1 + arr2 + arr3).count(x) > 2]
    
    def arraysIntersection2(self, arr1, arr2, arr3):
        if len(arr1) >= len(arr2):
            if len(arr3) >= len(arr1):
                maxarr = arr3
                midarr = arr1
                minarr = arr2
            else:
                if len(arr3) >= len(arr2):
                    maxarr = arr1
                    midarr = arr3
                    minarr = arr2
                else:
                    maxarr = arr1
                    midarr = arr2
                    minarr = arr3

        ret_ = self.findcommonnum(minarr, midarr)
        ret = self.findcommonnum(ret_, maxarr)
        return ret


    def findcommonnum(self, arr1, arr2):
        p1 = 0
        p2 = 0
        ret = list()
        while p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1] == arr2[p2]:
                ret.append(arr1[p1])
                p1 += 1
                p2 += 1
            elif arr1[p1] > arr2[p2]:
                p2 += 1
            else:
                p1 += 1
        return ret

if __name__=='__main__':
    sol = Solution()
    arr1 =  [1,2,3,4,5]
    arr2 = [1,2,5,7,9]
    arr3 = [1,3,4,5,8]
    print(sol.arraysIntersection2(arr1, arr2, arr3))