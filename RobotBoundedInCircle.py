class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = ['N','W','S','E']
        init_pos = ['E', [0,0]]
        pos =['E', [0,0]]
        n = len(instructions)
        def move(command):
            if command == 'G':
                if pos[0] == 'N': pos[1][1] += 1
                elif pos[0]== 'S': pos[1][1] -= 1
                elif pos[0] == 'W': pos[1][0] -= 1
                else: pos[1][0] += 1
            elif command == 'L':
                pos[0] = direction[(direction.index(pos[0]) - 1) % 4]
            else:
                pos[0] = direction[(direction.index(pos[0]) + 1) % 4]
        count = 0
        while True:
            if count > 0 and count % n == 0 and pos[0] == init_pos[0]:
                break
            move(instructions[count % n])
            count += 1
            
        if init_pos[1] == pos[1]:
            return True
        else:
            return False

if __name__=='__main__':
    sol = Solution()
    ins = 'GG'
    print(sol.isRobotBounded(ins))
