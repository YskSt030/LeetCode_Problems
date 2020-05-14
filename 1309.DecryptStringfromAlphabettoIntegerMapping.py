class Solution:
    def freqAlphabets(self, s: str) -> str:
        ret = ''
        numa = ord('a') - 1
        i = 0
        while i < len(s):
            if s[i] == '0':
                debug = ret[:-1]
                ret = ret[:-1] + chr(int(s[i-1]) * 10 + numa )
                i += 2
            elif s[i] == '#':
                ret = ret[:-2] + chr(int(s[i-2])  * 10 + int(s[i-1]) + numa )
                i += 1
            else:
                ret += chr(int(s[i]) + numa)
                i += 1
        return ret
    def freqAlphabets_2(self, s: str) -> str:
        nums = s.split('#')
        numa = ord('a') - 1
        ret = ''
        for i in range(len(nums) - 1):
            if len(nums[i]) > 2:
                for j in range(0, len(nums[i]) - 2):
                    ret += chr(int(nums[i][j]) + numa)
            ret +=  chr(int(nums[i][len(nums[i] - 2)])  * 10 + int(nums[i][len(nums[i] - 1)]) + numa)
        if s[-1] == '#':
            if len(nums[-1]) > 2:
                for j in range(0, len(nums[-1]) - 2):
                    ret += chr(int(nums[-1][j]) + numa)
            ret +=  chr(int(nums[-1][len(nums[-1] - 2)])  * 10 + int(nums[-1][len(nums[-1] - 1)]) + numa)
        else:
            for j in range(len[nums[-1]]):
                ret += chr(int(nums[-1][j]) + numa)
        return ret

if __name__ == '__main__':
    sol = Solution()
    str_in = "10#11#12"
    print(sol.freqAlphabets_2(str_in))