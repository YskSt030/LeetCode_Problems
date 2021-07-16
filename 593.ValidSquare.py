import itertools
class Solution:
    def validSquare(self, p1,p2,p3,p4) -> bool:
        P = [p1,p2,p3,p4]
        for p in itertools.combinations(P,2):
            q = P.copy()
            q.remove(p[0])
            q.remove(p[1])
            if (p[0][0] - p[1][0] )** 2 + (p[0][1] - p[1][1] )** 2 == (q[0][0] - q[1][0] )** 2 + (q[0][1] - q[1][1] )** 2:
                if p[0][0] !=  p[1][0] and q[0][0] != q[1][0]:
                    if (p[0][1] - p[1][1] ) * (q[0][1] - q[1][1] ) // (p[0][0] - p[1][0] ) // (q[0][0] - q[1][0] ) == -1:
                        return True
                elif p[0][0] ==  p[1][0] and q[0][1] == q[1][1]:
                    return True
                elif q[0][0] ==  q[1][0] and p[0][1] == p[1][1]:
                    return True
        return False

if __name__=='__main__':
    sol = Solution()
    #p1, p2, p3, p4 = [0,0], [1,1], [1,0], [0,1]
    p1, p2, p3, p4 = [1,0], [-1,0], [0,1], [0,-1]

    print(sol.validSquare(p1, p2, p3, p4 ))
                        