'''
inputs:
    - prices - array of prices as ints
output:
    - max profit to achieve when you buy a neetcode then sell it to some day in the future


examples:
 - [10, 9, 8, 7] ==> always operating at a loss so you never buy so return 0
 - [1, 2, 3, 4, 5] ==> always operating at a gain so you buy first day and sell on last day getting 4 as profit

Observations
* whenever you buy neetcoin, you operate at a loss
    * so you negate the value that you buy... for example, on 2nd index day, you buy at 5 which means you are at a loss of -5 neetcoin


Brute force algorithm O(N^2) 
* you buy at day i, then attempt to sell for all other days and pick the max you can get from that simulation, and repeat until you reach the end of prices to obtain the max...

O(N) solution?
* how to apply Kadane's Algorithm???
    1. current_sum
    2. best_sum


* buy_price == something you bought in the past (minimize)
* sell_price == something you will sell in the future (maximize)

net_diff = sell_price - buy_price

* net_diff < 0 --> operate at loss
* net_diff == 0 --> breaking even
* net_diff > 0 --> operating at a profit

kadane algorithm:
* current_sum = max(x, current_sum + x)
* best_sum = max(current_sum, best_sum)


current_sum = 0
best_sum = 0

buy_price = 10
sell_price = 1, 5, 6, 7, 1

- initialize buy_price = prices[0]
- initialize sell_price = prices[1]

curr_net_diff = float('-inf')
sell_price = float('-inf')

net_diff = sell_price - buy_price

curr_net_diff = max(curr_net_diff, net_diff)
best_net_diff = max(best_net_diff, curr_net_diff)


i = 0
sell_price = min(prices[i], sell_price) = 10
buy_price = prices[i] = 10
net_diff = buy_price - sell_price

curr_net_diff = max(-inf, 10 - 10) = 0
best_net_diff = max(-inf, 0) = 0

i = 1
sell_price = min(1, 10) = 1
buy_price = 1
net_diff = 0

curr_net_diff = max(0, 1 - 1) = 0
best_net_diff = max(0, 0) = 0

i = 2
sell_price = min(1, 5) = 1
buy_price = 5
net_diff = 5 - 1 = 4
curr_net_diff = max(0, 4) = 4
best_net_diff = max(0, 4) = 4


i = 2
sell_price = min(1, 6) = 1
buy_price = 6
net_diff = 6 - 1 = 5
curr_net_diff = max(4, 6) = 6
best_net_diff = max(4, 6) = 6

i = 3
sell_price = min(1, 7) = 1
buy_price


[3,1,2,8,9,4,1,6,10]



'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_price = float('inf')
        buy_price = float('-inf')
        best_net_diff = 0

        for i in range(len(prices)):
            sell_price = min(sell_price, prices[i])
            buy_price = prices[i]

            net_diff = buy_price - sell_price
            best_net_diff = max(net_diff, best_net_diff)
        
        return best_net_diff