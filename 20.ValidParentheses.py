"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s):
        d = {"(":")","{":"}","[":"]"}
        l = list()
        for c in s:
            if c in d.keys():
                l.append(c)
            else:
                if len(l) == 0:
                    return False
                if d[l[-1]] == c:
                    l.pop()
                else:
                    return False
        if len(l) == 0:
            return True
        else:
            return False