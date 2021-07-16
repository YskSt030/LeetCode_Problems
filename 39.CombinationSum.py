"""
Given a set of candidate numbers (candidates) (without duplicates) and a
 target number (target), find all unique combinations in candidates 
 where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
Each element of candidate is unique.
1 <= target <= 500
"""

class Solution:
    def combinationSum(self, candidates, target: int) :
        self.ret = list()
        def find(list_, candidates_, target_):
            for c in candidates_:
                if target_ - c == 0:
                    list_ret = list_.copy()
                    list_ret.append(c)
                    list_ret.sort()
                    if list_ret not in self.ret:
                        self.ret.append(list_ret)
                elif target_ - c > 0:
                    list_next = list_.copy()
                    list_next.append(c)
                    list_next.sort()
                    find(list_next, candidates_, target_ - c)
        l = list()
        find(l, candidates, target)
        return self.ret
