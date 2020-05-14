"""
Given two integers dividend and divisor, 
divide two integers without using multiplication, 
division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers 
within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 
31 − 1 when the division result overflows.
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
            MAXNUM = 2 ** 31 - 1
            MINNUM = -(2 ** 31)
            ret = 0
            num = 0
            
            if dividend > 0 and divisor < 0:
                while True:
                    if dividend == num:
                        break
                    if dividend < num:
                        ret += 1
                        break
                    num -= divisor
                    if num < MINNUM:
                        return MINNUM
                    ret -= 1
            elif dividend < 0 and divisor > 0:
                while True:
                    if dividend == num:
                        ret = ret
                        break
                    if dividend > num:
                        ret += 1
                        break
                    num -= divisor
                    if num < MINNUM:
                        return MINNUM
                    ret -= 1
            elif dividend < 0 and divisor < 0 or dividend > 0 and divisor > 0:
                while True:
                    if dividend == num:
                        break
                    if dividend < num:
                        ret -= 1
                        break
                    num += divisor
                    if num > MAXNUM:
                        return MAXNUM
                    ret += 1
            return ret
           
if __name__== '__main__':
    sol = Solution()
    diviend = 7
    divisor = -3
    print(sol.divide(diviend,divisor))

                
        