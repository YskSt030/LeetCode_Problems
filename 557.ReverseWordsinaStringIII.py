"""
Given a string, you need to reverse the order of characters in each word
within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        ret = ""
        if s == None:
            return None
        elif len(s) == 1:
            return s
        else:
            for i in range(len(s)):
                if s[i] == ' ':
                    ret += self.reverseWord(word) + ' '
                    word = ""
                else:
                    word += s[i]
            ret += self.reverseWord(word)#Last
            return ret

    def reverseWord(self, s: str) -> str:
        ret = ""
        for i in range(len(s)):
            ret += s[len(s)-i-1]
        return ret

if __name__ == '__main__':
    sol = Solution()
    str_ = "Hello World"
    print(sol.reverseWords(str_))

