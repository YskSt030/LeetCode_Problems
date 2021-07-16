class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        D = defaultdict(int)
        D[s[0]] = 1
        p,q = 0,0
        ret = 0
        while True:
            q += 1
            if q == len(s):
                ret = max(ret, q - p)
                break
            D[s[q]] += 1
            while D[s[q]] > 1:
                p += 1
                D[s[p]] -= 1
            
            ret = max (ret, q - p + 1)
        return ret
if __name__=='__main__':
    sol = Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))