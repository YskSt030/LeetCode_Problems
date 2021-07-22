class Solution:
    def partitionDisjoint(self, nums) -> int:
        MINS,MAXS = [0] * len(nums), [0]*len(nums)
        MINS[-1] = nums[-1]
        MAXS[0] = nums[0]
        for i in range(1,len(nums)):
            MAXS[i] = max(nums[i],MAXS[i-1])
            MINS[len(nums)-i-1] = min(nums[len(nums)-i-1], MINS[len(nums)-i])
        p = 0
        while MAXS[p] > MINS[p + 1]:
            p += 1
            if p == len(nums) - 1:
                return len(nums)
        return p + 1

if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,1,0,6,12]
    print(sol.partitionDisjoint(nums))