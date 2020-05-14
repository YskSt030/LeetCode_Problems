"""
Given a string S, return the number of substrings 
that have only one distinct letter.

Example 1:
Input: S = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.

Example 2:
Input: S = "aaaaaaaaaa"
Output: 55
 

Constraints:

1 <= S.length <= 1000
S[i] consists of only lowercase English letters.
"""

class Solution:
    def countLetters(self, S: str) -> int:
        p = 0
        p_r = p
        ret = 0
        def countnum(n: int) -> int:
            return (n + 1) * n //2
        while p < len(S):
            while S[p] == S[p_r]:
                p_r += 1
                if p_r == len(S):
                    break
            ret += countnum(p_r - p) 
            p = p_r
        return ret

if __name__=='__main__':
    sol = Solution()
    S = 'aaaba'
    print(sol.countLetters(S))