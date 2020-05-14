class Solution:
    def isArmstrong(self, N: int) -> bool:
        digits = len(str(N))
        culcval = 0
        for i in range(digits):
            culcval += int(str(N)[i]) ** digits
        return culcval == N

if __name__ == '__main__':
    sol = Solution()
    num_in = 153
    print(sol.isArmstrong(num_in))