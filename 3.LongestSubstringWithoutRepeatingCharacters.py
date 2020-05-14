

"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p_a ,p_b = 0, 0
        len_s = len(s)
        maxlen = -1
        wlist = set()
        if len(s) < 2:
            return len(s)
        while p_b < len(s):
            if s[p_b] not in wlist:
                wlist.add(s[p_b])
                p_b += 1
                maxlen = max(maxlen, p_b - p_a )
            else:
                wlist.remove(s[p_a])
                p_a += 1
                maxlen = max(maxlen, p_b - p_a + 1)
        return maxlen


if __name__ == '__main__':
    
    sol = Solution()
    s = 'pwwkew'
    s2 = s[2:6]
    ret = sol.lengthOfLongestSubstring(s)
    debug = 1
    