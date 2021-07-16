"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution:    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ""
        if len(strs) is 0:
            return ""
        elif len(strs) is 1:
            return strs[0]
        else:
            lenstr = [len(str_) for str_ in strs]
            minlen = min(lenstr)
            for i in range(1,minlen+1):
                for str_ in strs:
                    if strs[0][:i] != str_[:i]:
                        return strs[0][:i-1]
                ret = strs[0][:i]
        return ret

if __name__ =='__main__':
    sol = Solution()
    strs = ["c","acc","ccc"]
    ret = sol.longestCommonPrefix(strs)
    debug = 1