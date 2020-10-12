"""
Given two strings A and B of lowercase letters, return true if you can swap two letters in A 
so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that 
i != j and swapping the characters at A[i] and A[j]. 
For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Example 1:
Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.

Example 2:
Input: A = "ab", B = "ab"
Output: false
Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.

Example 3:
Input: A = "aa", B = "aa"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.

Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:
Input: A = "", B = "aa"
Output: false
 
Constraints:
0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist of lowercase letters.
"""

from collections import defaultdict
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) == len(B) and len(A) >= 2:
            a_,b_ = "", ""
            chars = defaultdict(int)
            for i in range(len(A)):
                if A[i] != B[i]:
                    a_ += A[i]
                    b_ += B[i]
                else:
                    chars[A[i]] += 1
            if len(a_) == 0:
                lists = list(chars.values())
                lists = [a for a in lists if a > 1]
                if len(lists) > 0:
                    return True
                else:
                    return False
            elif len(a_) == 2 and a_[0] == b_[1] and b_[0] == a_[1]:
                return True
            else:
                return False
        return False
        
if __name__ == '__main__':
    sol = Solution()
    A, B = "ab", "ba"
    print(sol.buddyStrings(A,B))