"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

Follow up:

What if the matrix is stored on disk, and the memory is limited such that
 you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial
row into the memory at once?
"""


class Solution:
    #def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
    def isToeplitzMatrix(self, matrix):
            ret = True
            m = len(matrix[0])
            n = len(matrix)

            for i in range(-n, m):
                templist = []
                if ret == True:
                    for j in range(n):
                        if i + j >= 0 and i + j < m:
                            # print('j;'+str(j)+',j+i:'+str(j+i)+',matrix val is;'+str(matrix[j][j+i]))
                            templist.append(matrix[j][j + i])
                            if len(templist) >= 2 and templist[-1] != templist[-2]:
                                ret = False
                                break
            return ret


if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,2,1],[1,1,1],[1,1,1]]
    ret = sol.isToeplitzMatrix(matrix)
    print(ret)