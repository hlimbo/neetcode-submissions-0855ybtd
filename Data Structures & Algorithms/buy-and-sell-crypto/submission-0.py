'''
Inputs:
* int array prices
* prices[i] = price of NeetCoin on the ith day

Decisions
1. pick 1 day to buy 1 NeetCoin
2. pick a different day in future to sell the coin
3. can choose not to buy or sell
* limitation: you can only make 1 choice per day

Task:
-> Return max profit you can achieve

buy on day 1
10  1   5   6   7   1
    -9  -5  -4 -3   -9

buy on day 2
1   5   6   7   1
    4   5   6   0

buy on day 3
5   6   7   1
    1   2  -4

buy on day 4
6   7    1
    1   -5

key insight: if its decreasing, then buying is on a loss
key insight 2: if its increasing, then buying is on an uphill win

One way to do it is to try simulating a purchase for each day and selling it on all other future days
* from there, you pick the outcome that yields the max profit

maxProfit = 0

for i in range(len(prices)):
    netAmount = 0
    for j in range(i+1,len(prices)):
        netAmount = prices[j] - prices[i]
        if netAmount > maxProfit:
            maxProfit = netAmount

return maxProfit      



'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxValue = 0
        for i in range(len(prices)):
            netAmount = 0
            for j in range(i+1, len(prices)):
                netAmount = prices[j] - prices[i]
                if netAmount > maxValue:
                    maxValue = netAmount
        
        return maxValue