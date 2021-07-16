"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into 
letters using the reverse of the mapping above (there may be multiple ways). For example, 
"11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be 
mapped into 'F' since "6" is different from "06".

In addition to the mapping above, an encoded message may contain the '*' character, 
which can represent any digit from '1' to '9' ('0' is excluded). For example, 
the encoded message "1*" may represent any of the encoded messages 
"11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1*" is 
equivalent to decoding any of the encoded messages it can represent.

Given a string s containing digits and the '*' character, return the number of ways to decode it.

Since the answer may be very large, return it modulo 109 + 7.


"""

class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        B = ['0','1','2','3','4','5','6']
        self.ret = 0
        def culc(s,v):
            if len(s) == 0:
                self.ret += v 
                self.ret % MOD
            elif len(s) == 1:
                if s[0] == '*':
                    v_ = (v*9) % MOD
                else:
                    v_ = v
                culc(s[1:],v_)
            else:
                a,b = s[0],s[1]
                if a != '0':
                    if a == '*':
                        v_ == (v * 9) % MOD
                    else:
                        v_ = v
                    culc(s[1:],v_)
                    if a == '1' or a == '2' or a == '*':
                        if a == '1':
                            if b == '*':
                                v_ = (v * 9) % MOD
                            else:
                                v_ = v
                        elif a == '2':
                            if b == '*':
                                v_ = (v * 6) % MOD
                            elif b in B:
                                v_ = v
                        elif a == '*':
                            if b == '*':
                                v_ = (v * 15) % MOD
                            elif b in B and b != '0':
                                v_ = (v * 2) % MOD
                            else:
                                v_ = v
                        culc(s[2:],v_)
        culc(s,1)
        return self.ret


if __name__=='__main__':
    sol = Solution()
    print(sol.numDecodings('2*'))