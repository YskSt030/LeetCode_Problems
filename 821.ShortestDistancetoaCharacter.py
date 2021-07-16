"""
Given a string S and a character C, return an array of integers
representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""


class Solution:
    def shortestToChar(self, S: str, C: str) -> list[int]:
        if len(S) < 1 or len(S) > 10000:
            return None
        else:
            index_c = []
            ret = []
            for i in range(len(S)):
                if S[i] == C:
                    index_c.append(i)
            num = range(index_c[0], -1, -1)
            ret.extend(num)
            for j in range(1, len(index_c)):
                len_ = index_c[j] - index_c[j - 1]
                print(len_)
                ret.extend(self.makedist(len_))
            if index_c[-1] < len(S):
                ret.extend(range(1, len(S) - index_c[-1], 1))
            return ret

        def makedist(self, n):
            if n <= 1:
                return [0]
            else:
                ret = []
                for i in range(n):
                    ret.append(min(i + 1, n - i - 1))
                return ret
    #20210207 added
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ret = [10**4 + 1] * len(s)
        for i , x in enumerate(s):
            if x == c:
                for j in range(len(s)):
                    ret[j] = min(ret[j], abs(i-j))
        return ret
if __name__ =='__main__':
    S = "iamagoodman"
    C = 'a'
    sol = Solution()
    print(sol.shortestToChar(S,C))