'''
Given a sorted integer array arr, two integers k and x, 
return the k closest integers to x in the array. 
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:
1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
'''

class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        N = len(arr)
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[-k:]
        else:
            p,q = 0,N - 1
            while p+1<q:
                m = (p+q)//2
                if arr[m] > x:
                    q = m
                else:
                    p = m
            ret = list()
            for i in range(k):
                if x - arr[p] <= arr[q] - x:
                    ret.append(arr[p])
                    p -= 1
                else:
                    ret.append(arr[q])
                    q += 1
                if q == N or p == -1:
                    break
            if len(ret) < k:
                numleft = k - len(ret) 
                if q == N:
                    for i in range(numleft):
                        ret.append(arr[p])
                        p -= 1
                else:
                    for i in range(numleft):
                        ret.append(arr[q])
                        q += 1
            ret.sort()
        return ret
 

if __name__=='__main__':
    sol = Solution()
    arr = [1,2,3,4,5]
    k = 4
    x = 3
    print(sol.findClosestElements(arr,k,x))
