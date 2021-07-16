"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.
On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.



Example 1:

Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.


Note:

1 <= N <= 1000
"""

class Solution:

    def divisorGame(self, N: int) -> bool:
        self.num = 0
        self.ret = False
        self.recursivedevision(N , 1)
        return self.ret
    def recursivedevision(self, N, num):
        if self.ret == False:
            if self.num % 2 == 0:
                print('next,Alice,N:'+str(N))
            else:
                print('next,Bob,N:' + str(N))
            ret_ = False
            for i in range(1,N):
                if self.ret == False and N % i == 0:
                    if self.num % 2 == 0:
                        print('Alice took:' + str(i))
                    else:
                        print('Bob,took:' + str(i))
                    ret_ = True
                    self.num += 1
                    self.recursivedevision(N - i, num + 1)
            if ret_ == False:
                print('Finished:' + str(num))
                print('')
                if num % 2 == 0:
                    self.ret = True




if __name__ == '__main__':
    sol = Solution()
    ret = sol.divisorGame(10)
    print (ret)