
class Solution:
    def grayCode(self, n: int):
        ret = [0]
        L = list(range(1,2**n))
        R = list()
        D = list()
        for i in range(n):
            D.append(2**i)
        for i in range(2**(n-1)-1):
            for l in L:
                if ret[-1] ^ l in D:
                    ret.append(l)
                    R.append(D.index(ret[-2] ^ l))
                    L.remove(l)
                    break
        for i in range(len(R)):
            num = (2**n-1) - 2**R[i]
            ret.append(ret[-1] & num)
        return ret[:-1]

if __name__=='__main__':
    sol = Solution()
    ret = sol.grayCode(4)
    print(ret)
    ret_bin = list()
    for r in ret:
        ret_bin.append(bin(r))
    print(ret_bin)