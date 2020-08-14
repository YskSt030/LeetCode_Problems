"""
Given a string which consists of lowercase or uppercase letters, 
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"
Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        C = collections.Counter(s)       
        ret = 0
        for c in C.keys():
            ret += (C[c] // 2) * 2
            C[c] = 1 if C[c] % 2 == 1 else 0
        C = [C[c] for c in C.keys()]
        if 1 in C:
            ret += 1
        return ret