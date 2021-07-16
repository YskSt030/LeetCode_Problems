"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- 
whose elements may also be integers or other lists.

Example 1:
Input: [[1,1],2,[1,1]]
Output: 10 
Explanation: Four 1's at depth 2, one 2 at depth 1.
E
xample 2:
Input: [1,[4,[6]]]
Output: 27 
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.
"""
class Solution:
    def depthSum(self, nestedList) -> int:
        return self.addnum(nestedList, 1)
    
    def addnum(self, list_, depth_):
        if type(list_) == int:
            return list_ * depth_
        elif type(list_) == list:
            ret = 0
            for i in range(len(list_)):
                if type(list_[i]) == int:
                    ret += list_[i] * depth_
                elif type(list_[i]) == list:
                    ret += self.addnum(list_[i], depth_ + 1)
            return ret

if __name__=='__main__':
    sol = Solution()
    nestedList = [[1,1],2,[1,1]]
    nestedList2 = [1,[4,[6]]]
    print(sol.depthSum(nestedList))
    print(sol.depthSum(nestedList2))