"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        l = [1,1]
        for i in range(2,rowIndex + 1):
            l_ = [1]
            for j in range(1, len(l)):
                l_.append(l[j - 1] + l[j])
            l_.append(1)
            l = l_.copy()
        return l