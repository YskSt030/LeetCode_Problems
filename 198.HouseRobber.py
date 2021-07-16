class Solution:
    def rob(self, nums) -> int:
        self.l = list()
        def add(list_, nums_):
            if len(nums_) == 0:
                self.l.append(sum(list_))
            elif len(nums_) == 1:
                self.l.append(sum(list_) + nums_[0])
            elif len(nums_) == 2:
                self.l.append(sum(list_) + max(nums_[0],nums_[1]))
            else:
                list_next = list_.copy()
                list_next.append(nums_[0])
                add(list_next, nums_[2:])
                list_next = list_.copy()
                add(list_next, nums_[1:])
        add([],nums)
        return max(self.l)
if __name__=='__main__':
    sol = Solution()
    nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,\
    186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112\
        ,78,135,62,228,247,211]
    print(sol.rob(nums))
