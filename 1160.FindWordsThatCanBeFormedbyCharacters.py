
"""
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from 
chars (each character can only be used once).
Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 
Note:
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
"""


class Solution:
    #def countCharacters(self, words: List[str], chars: str) -> int:
    def countCharacters(self, words, chars: str) -> int:
        Clist = self.makelist(chars)
        ret = 0
        for word in words:
            Wlist = self.makelist(word)
            for i in range(26):
                if Wlist[i] > Clist[i]:
                    break
                if i == 25:
                    ret += len(word)
        return ret
    def makelist(self, words):
        S = 'abcdefghijklmnopqrstuvwxyz'
        ret = [0] * 26
        for w in words:
            ret[S.index(w)] += 1
        return ret 

    def checkValidString(self, s: str) -> bool:
        pval = [0]
        if len(s) == 0:
            return True
        elif len(s) == 1 and s[0] != '*':
            return False
        elif len(s) == 1 and s[0] == '*':
            return True
        else:
            for c in s:
                if c == '*':
                    temp_ = list()
                    for p in range(len(pval)):
                        temp_.extend([pval[p]+1,pval[p]-1])
                    pval.extend(temp_)
                elif c == '(':
                    for p in range(len(pval)):
                        pval[p] += 1
                else:
                    for p in range(len(pval)):
                        pval[p] -= 1
                pval = [p for p in pval if p >= 0]
            if 0 in pval:
                return True
            else:
                return False                
    def findMaxLength(self, nums) -> int:
        Slist = dict()
        Slist[0] = [0]
        s = 0
        for i in range(len(nums)):
            s += -1 + 2 * nums[i]
            if s not in Slist.keys():
                Slist[s] = [i+1]
            else:
                Slist[s].append(i+1)
        ret = 0       
        for S in Slist.values():
            temp = S[-1] - S[0] 
            if temp > ret:
                ret = temp
        return ret

if __name__=='__main__':
    sol = Solution()
    words = ["cat","bt","hat","tree"]
    chars = 'atach'
    s = '(())((())()()(*)(*()(())())())()()((()())((()))(*'
    nums = [0 ,1 ]
    print(sol.findMaxLength(nums))