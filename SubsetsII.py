class Solution:
    def subsetsWithDup(self, nums):
        N = len(nums)
        ret = list()
        for i in range(2**N):
            q = i
            tmp = list()
            d = 0
            while q > 0:
                if q % 2 == 1:
                    tmp.append(nums[d])
                q //= 2
                d += 1
            tmp.sort()
            if tmp not in ret:
                ret.append(tmp)
        return list(ret)

if __name__=='__main__':
    sol = Solution()
    nums = [1,2,2]
    print(sol.subsetsWithDup(nums))