"""Given a character array s, reverse the order of the words.
A word is defined as a sequence of non-space characters. 
The words in s will be separated by a single space.
Your code must solve the problem in-place, 
i.e. without allocating extra space.

Example 1:
Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Example 2:
Input: s = ["a"]
Output: ["a"]
"""
class Solution:
    def reverseWords(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p,q = 0, len(s)-1
        while p + 1 <= q:
            s[p],s[q] = s[q],s[p]
            p,q = p+1,q-1
        
        def rev_(p,q):
            while p + 1 <= q:
                s[p],s[q] = s[q],s[p]
                p,q = p+1,q-1
        L = list()
        for i in range(len(s)):
            if s[i] == ' ':
                L.append(i)
        if len(L) == 0:
            rev_(0,len(s)-1)
        else:
            for i in range(len(L)):
                if i == 0:
                    rev_(0,L[i]-1)
                else:
                    rev_(L[i-1]+1,L[i]-1)
            rev_(L[-1]+1, len(s)-1)

if __name__=='__main__':
    Sol = Solution()
    l = ['h','i']
    Sol.reverseWords(l)
    print(l)