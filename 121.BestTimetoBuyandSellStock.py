"""
Say you have an array for which the ith element is the 
price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.


Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minnum = -1
        maxnum = -1
        maxind = -1
        maxval = 0
        for i in range(len(prices) ):
            if minnum < 0 or prices[i] < minnum:
                minnum = prices[i]
                if maxind < i:
                    maxnum = minnum
            if prices[i] > maxnum:
                maxnum = prices[i]
                maxind = i
                if maxval < maxnum - minnum:
                    maxval = maxnum - minnum
        return maxval

if __name__=='__main__':
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))