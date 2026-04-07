class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxValue = 0
        # l represents the day you buy
        # r represents the day you sell
        l, r = 0, 1
        while r < len(prices):
            isAtLoss = prices[r] - prices[l] < 0
            if isAtLoss:
                l = r
                r += 1
            else:
                # either gaining or staying at same profit
                maxValue = max(prices[r] - prices[l], maxValue)
                r += 1

        return maxValue