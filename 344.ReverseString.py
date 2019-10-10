"""
Write a function that reverses a string.
The input string is given as an array of characters char[].

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        count = len(s)
        count_ = 0
        if count == 0:
            return []
        elif count == 1:
            return s
        else:
            while count_ <= len(s)-count_-1:
                temp = s[count_]
                s[count_] = s[len(s)-count_-1]
                s[len(s) - count_ - 1] = temp
                count_ += 1

if __name__=='__main__':
    s_ = ['h','e','l','l','o']
    sol = Solution()
    sol.reverseString(s_)
    print(s_)