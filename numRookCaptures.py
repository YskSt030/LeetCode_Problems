"""
On an 8 x 8 chessboard, there is one white rook.
There also may be empty squares, white bishops, and black pawns.
These are given as characters 'R', '.', 'B', and 'p' respectively.
Uppercase characters represent white pieces,
and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions
(north, east, west, and south), then moves in that direction
until it chooses to stop, reaches the edge of the board, or
captures an opposite colored pawn by moving to the same square it occupies.
Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

"""
import sys
class Solution:
    BSIZE = 8
    def numRookCaptures(self, board: list[list[str]]) -> int:
        ret = 0
        for i in range(self.BSIZE):
            for j in range(self.BSIZE):
                if board[i][j] == 'R':
                    ret = ret + self.findPawns(i, j, board)
        return ret

    def findPawns(self, i, j, board: list[list[str]]) -> int:
        ret = 0
        p = 1
        while i + p < self.BSIZE :
            if board[i+p][j] == 'B':
                break
            elif board[i+p][j] == 'p':
                ret = ret + 1
                break
            p = p + 1
        p = 1
        while i - p >= 0 :
            if board[i-p][j] == 'B':
                break
            elif board[i-p][j] == 'p':
                ret = ret + 1
                break
            p = p + 1
        p = 1
        while j + p < self.BSIZE :
            if board[i][j+p] == 'B':
                break
            elif board[i][j+p] == 'p':
                ret = ret + 1
                break
            p = p + 1
        p = 1
        while j - p >= 0:
            if board[i][j-p] == 'B':
                break
            elif board[i][j-p] == 'p':
                ret = ret + 1
                break
            p = p + 1
        return ret


if __name__ == "__main__":
    sol_ = Solution()
