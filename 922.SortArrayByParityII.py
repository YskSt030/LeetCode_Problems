"""
922. Sort Array By Parity II

Given an array A of non-negative integers,
half of the integers in A are odd, and half of the integers are even.
Sort the array so that whenever A[i] is odd,
i is odd; and whenever A[i] is even, i is even.
You may return any answer array that satisfies this condition.

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5]
would also have been accepted.

Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000

"""


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ret = []
        # count the number that filled the ret list by odd/ even respectly
        # actual index of list is
        # oddnum: count_odd * 2
        # evennum: count_even * 2 + 1
        count_odd = 0
        count_even = 0
        if len(A) <= 20000:
            for i in range(len(A)):
                if A[i] % 2 == 0:
                    count_even += 1
                    fill_num = max(0, count_even * 2 - 1 - len(ret))
                    for j in range(fill_num):
                        ret.append(-1)
                    ret[(count_even - 1) * 2] = A[i]
                else:
                    count_odd += 1
                    fill_num = max(0, count_odd * 2 - len(ret))
                    for j in range(fill_num):
                        ret.append(-1)
                    ret[(count_odd - 1) * 2 + 1] = A[i]
        return ret
