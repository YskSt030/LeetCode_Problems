"""
Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        p_a = 0
        p_b = 0
        maxlen = 0
        ret = ""
        if len(s) < 2:
            return len(s)
        else:    
            while p_b < len(s):
                if self.isPalindrome(s[p_a:p_b+1]):
                    if p_b + 1 - p_a > maxlen:
                        maxlen = p_b + 1 - p_a 
                        ret = s[p_a:p_b+1]
                    p_b += 1
                else:
                    p_a += 1
                    #
                    if p_a > p_b:
                        p_b+=1
        return ret
            
    def isPalindrome(self, s):
        p_a = 0
        p_b = len(s) - 1
        while p_a < p_b:
            if s[p_a] != s[p_b]:
                return False
            p_a += 1
            p_b -= 1
        return True

if __name__=='__main__':
    sol = Solution()
    s = "babad"
    ret = sol.longestPalindrome(s)
    print(ret)
  