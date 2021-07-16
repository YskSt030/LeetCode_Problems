"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

import itertools
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = list()
        for r in itertools.combinations(list(range(n * 2)),n):
            l_ = ''
            st = 0
            for i in range(2 * n):
                if i in r:
                    l_ += '('
                    st += 1
                else:
                    l_ += ')'
                    st -= 1
                    if st < 0:
                        break
                    if i == 2 * n - 1 and st == 0:
                        ret.append(l_)
        return ret