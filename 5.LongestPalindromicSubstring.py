"""
Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bbt
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        wlist = dict()
        maxlen = 1
        ret = s[0]
        for i in range(len(s)):
            if s[i] not in wlist.keys():
                wlist[s[i]] = [i]
            else:
                wlist[s[i]].append(i)
        for c in wlist.keys():
            if len(wlist[c]) > 1:
                for i in range(len(wlist[c])-1):
                    for j in range(i+1, len(wlist[c])):
                        if self.isPalindrome(s[wlist[c][i]:wlist[c][j]+1]) and maxlen < wlist[c][j] - wlist[c][i] + 1:
                            ret = s[wlist[c][i]:wlist[c][j]+1]
                            maxlen = wlist[c][j] - wlist[c][i] + 1
        return ret
   
    def isPalindrome(self,s):
        p,q = 0, len(s) - 1
        while p < q:
            if s[p] != s[q]:
                return False
            p += 1
            q -= 1
        return True

if __name__=='__main__':
    sol = Solution()
    s = "babadada"
    ret = sol.longestPalindrome(s)
    print(ret)
  