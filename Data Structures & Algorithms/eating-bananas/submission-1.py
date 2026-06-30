'''
inputs:
* array piles
* index i represents the ith pile
* piles[i] represents the number of bananas in 1 pile
* h = number of hours you have to eat all bananas


* can decide bananas-per-hour eating rate of k
* each hour you may choose a pile of bananas and eats k bananas from that pile


* constraints
if pile has less than k bananas, you may finish eating the pile but cannot eat from another pile in same hour

Task
* return min integer k such that you can eat all bananas within h hours

Questions:
* is it possible that min integer k cannot be found?
* if k can be found, can the actual time koko eats all the banana piles be less than or equal to h hours?
* do you need to finish eating all the banana piles at exactly h hours? no

one way to solve this problem is to assume that k is max of piles
* simulated eating time >= h, decrement k by 1
* keep on doing this until simulated eating time < h, if that's the case then the min eating rate would be the k + 1


max(piles) = k
O(k * n) -- brute force

to apply binary search we can look for the min eating rate and max eating rate
* (I'll do this one first) this can be done by locating min and max banana piles, adding them up, and dividing it by 2 to get the average
* another way would be to obtain the average of all the piles but you would floor it so no decimal places for the banana eating rate is possible

floor (10 / 4) = 2

O(n * log(k)) where k is the banana eating rate


if eating simulation time > h, lower banana limit = banana eating rate
if eating simulation time == h, upper banana limit = banana eating rate

if eating simulation time < h, banana eating rate is met

recompute banana eating rate = (lower banana limit + upper banana limit) // 2
-- keep on going while lower banana limit < upper banana limit

'''
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upperBound = max(piles)
        lowerBound = 1

        # banana eating rate
        k = upperBound
        print(f"k starts at {k}")
        while lowerBound <= upperBound:
            # print(f"lower bound: {lowerBound}")
            # print(f"upper bound: {upperBound}")
            mid = (upperBound + lowerBound) // 2
            
            eatingSimTime = 0

            for pile in piles:
                eatingSimTime += math.ceil(pile / mid)

            if eatingSimTime > h:
                lowerBound = mid + 1
            elif eatingSimTime <= h:
                k = mid
                print(f"k now at {k}")
                upperBound = mid - 1

        return k
        