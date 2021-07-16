"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter
        C = Counter(s)
        tmp = list()
        for k in C.keys():
            if C[k] % 2 == 1:
                tmp.append(k)
        if len(tmp) < 2:
            return True
        return False