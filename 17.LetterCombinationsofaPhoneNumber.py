"""
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is 
given below. Note that 1 does not map to any letters.
(Image of phone buttons)


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, 
your answer could be in any order you want.
"""
class Solution:
    #def letterCombinations(self, digits: str) -> List[str]:
    #2:abc, 3:def, 4:ghi, 5:jkl, 6:mno, 7:pqrs, 8:tuv, 9:wxyz
    def letterCombinations(self, digits) :
        ret = list()
        for i in range(len(digits)):
            previous_len = len(ret)
            if digits[i] != '1':
                charlist = self.digitToLetterList(digits[i])
                if len(ret) == 0:
                    ret.extend(charlist)
                else:
                    for j in range(len(ret)):
                        for k in range(len(charlist)):    
                            ret.append(ret[j]+charlist[k])
            ret = ret[previous_len:]
        return ret


    def digitToLetterList(self, letter):
        ret = list()
        if letter == '2':
            ret = ['a', 'b', 'c']
        elif letter == '3':
            ret = ['d', 'e', 'f']
        elif letter == '4':
            ret = ['g', 'h', 'i']
        elif letter == '5':
            ret = ['j', 'k', 'l']
        elif letter == '6':
            ret = ['m', 'n', 'o']
        elif letter == '7':
            ret = ['p', 'q', 'r', 's']
        elif letter == '8':
            ret = ['t', 'u', 'v']
        elif letter == '9':
            ret = ['w', 'x', 'y', 'z']
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(chr(ord('a')+1))
    input_num = '23'
    ret = sol.letterCombinations(input_num)
    print(ret) 