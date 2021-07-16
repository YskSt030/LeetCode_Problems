class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ret = ''
        if numRows < 3:
            N_Group = numRows
        else:
            N_Group = numRows + numRows - 2
        
        for row in range(numRows):
            i = 0
            while True:
                if i + row < len(s):
                    ret += s[i + row]
                else:
                    break
                if row > 0 and row < numRows - 1:
                    if i + N_Group - row  < len(s):
                        ret += s[i + N_Group - row]
                    else:
                        break
                i += N_Group
        return ret
            
            
if __name__ == '__main__':
	sol = Solution()
	s = "PAYPALISHIRING"
	ret = sol.convert(s, 4)
	print(ret)
	
