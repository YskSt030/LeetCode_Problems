"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 
when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x: int) -> int:
        rs = str(x)[::-1]
		
        if rs.endswith('-'):
            rs = '-' + rs[:-1]
			
        return 0 if int(rs) > 2147483647 or int(rs) < -2147483648 else int(rs)

if __name__ == "__main__":
    sol = Solution()
    num = 120
    print(sol.reverse(num))