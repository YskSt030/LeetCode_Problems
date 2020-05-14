""" 
Given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:
Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.

Example 2:
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.

Example 3:
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
 

Constraints:

1 <= num <= 10^4
num's digits are 6 or 9.

"""

class Solution:
    #Answer 1 use int -> str convertion
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        ret_str = str_num
        for i in range(len(str_num)):
            if str_num[i] == '6':
                ret_str = str_num[:i] + '9' + str_num[i+1:]
                break
        return int(ret_str)
    
    def maximum69Number_2 (self, num: int) -> int:
        num = num
        digit = 0
        ch_digit = -1
        while True:
            if (num // (10 ** digit)) % 10 == 6:
                ch_digit = digit
            if num > 10 ** digit and num < 10 ** (digit + 1):
                break
            digit += 1
        if ch_digit < 0:
            return num
        else:
            return num + 3 * (10 ** ch_digit)

if __name__ == '__main__':
    sol = Solution()
    num = 9669
    ret = sol.maximum69Number(num)
    ret2 = sol.maximum69Number_2(num)
    print(ret2)