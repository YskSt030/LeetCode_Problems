'''
You are given an integer length and an array updates where 
updates[i] = [startIdxi, endIdxi, inci].

You have an array arr of length length with all zeros, and 
you have some operation to apply on arr. In the ith operation, 
you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., 
arr[endIdxi] by inci.

Return arr after applying all the updates.

Example 1:
Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]

Example 2:
Input: length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]
Output: [0,-4,2,2,2,4,4,-4,-4,-4]
 
Constraints:
1 <= length <= 105
0 <= updates.length <= 104
0 <= startIdxi <= endIdxi < length
-1000 <= inci <= 1000
'''

class Solution:
    def getModifiedArray(self, length: int, updates):
        ret = [0]*length
        for i in range(len(updates)):
            tmp = updates[i]
            a,b,c = tmp[0],tmp[1],tmp[2]
            ret[a] += c
            if b < len(ret) - 1:
                ret[b + 1] += -c
        num = 0
        S = [0]*length
        for i in range(len(ret)):
            num += ret[i]
            S[i] = num
        return S

if __name__=='__main__':
    sol = Solution()
    length, updates = 10,[[2,4,6],[5,6,8],[1,9,-4]]
    print(sol.getModifiedArray(length, updates))