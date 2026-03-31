# counting problem
# what programming concepts can I use to solve this problem?
# from experience, I know that I can use recursion to count the number of ways to reach the nth stair

# recursion
# base case:
# stepCount == n
#   found 1 way to reach the nth stair
# stepCount > n
#   this way of doing it is invalid

# recursive step (choices):
# - take 1 step forward
# - take 2 steps forward
# each recursive step means we increase the step count either by 1 step or 2 steps to get closer to the nth step

# time complexity for this one would be O(2^N) where N is number of steps and 2 is the number of decisions we make
# we either take 1 step or 2 steps to climb the stairs

# n = 10
# climb 1 step at a time (one way)
# climb 2 steps at a time (2 ways)
# climb with a mix of using 1 step and 2 steps (this is the part where I have to count all possibilities)

class Solution:
    def helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 0:
            return 1
        
        if n < 0:
            return 0

        # if we already solved this sub problem when counting the number of ways to climb the stairs
        if n in memo:
            return memo[n]

        ways = self.helper(n-1, memo) + self.helper(n-2, memo)
        memo[n] = ways
        return memo[n]

    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)