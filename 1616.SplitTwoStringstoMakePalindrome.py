"""
You are given two strings a and b of the same length. Choose an index and split 
both strings at the same index, splitting a into two strings: 
aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: 
bprefix and bsuffix where b = bprefix + bsuffix. 
Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is 
allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , 
and "abc" + "" are valid splits.

Return true if it is possible to form a palindrome string, otherwise return false.

Notice that x + y denotes the concatenation of strings x and y.
 

Example 1:
Input: a = "x", b = "y"
Output: true
Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.

Example 2:
Input: a = "abdef", b = "fecab"
Output: true

Example 3:
Input: a = "ulacfd", b = "jizalu"
Output: true
Explaination: Split them at index 3:
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.

Example 4:
Input: a = "xbdef", b = "xecab"
Output: false
 
Constraints:
1 <= a.length, b.length <= 105
a.length == b.length
a and b consist of lowercase English letters
"""
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def isparindrome(a):
            if len(a) <= 1:
                return True
            n = len(a) // 2 + 1 if len(a) % 2 == 1 else len(a) // 2
            n_ = len(a) - 1
            for i in range(n+1):
                if a[i] != a[n_ - i]:
                    return False
            return True
        N = len(a) - 1
        ia,ib = -1,-1
        for i in range(N):
            if a[i] != b[N-i] and ia == -1:
                ia = i
            if b[i] != a[N-i] and ib == -1:    
                ib = i
            if ia >= 0 and ib >= 0:
                break
        if ia > ib:
            if isparindrome(b[ia:N-ia + 1]) == False:
                return isparindrome(a[ia:N-ia + 1])
            else:
                return True
        else:
            if isparindrome(a[ib:N-ib + 1]) == False:
                return isparindrome(b[ib:N-ib + 1])
            else:
                return True

if __name__=='__main__':
    sol = Solution()
    a, b = "x", "y"
    print(sol.checkPalindromeFormation(a,b))