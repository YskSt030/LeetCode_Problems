"""
Given a List of words, return the words that can be typed
using letters of alphabet on only one row's of
American keyboard like the image below.
(image)
Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]


Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

"""


class Solution:
    keyboard_lists = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                      ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
                      ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
    def findWords(self, words: list[str]) -> list[str]:
        ret = []
        if len(words) > 0:
            for i in range(len(words)):
                if len(words[i]) == 0:
                    continue
                num = [j for j in range(len(self.keyboard_lists)) if words[i][0].lower() in self.keyboard_lists[j]][0]
                if self.isintheRow(words[i], num):
                    ret.append(words[i])
        return ret

    def isintheRow(self, word, num):
        if len(word) == 0:
            return False
        else:
            ret = True
            for i in range(len(word)):
                if not word[i].lower() in self.keyboard_lists[num]:
                    ret = False
                    break
            return ret

if __name__ == '__main__':
    sol = Solution()
    wordlists = ['asd','aws','zxc','a','awidjfnv']
    ret = sol.findWords(wordlists)