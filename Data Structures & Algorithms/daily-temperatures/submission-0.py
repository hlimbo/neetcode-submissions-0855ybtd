'''
inputs:
* array of temperatures where the index or i represents the day the temperature is recorded
* e.g. temperatures[3] = 86 (86 degrees on 3rd day)

Outputs:
* return array result where result[i] 
is number of days AFTER ith day BEFORE a warmer temp appears on future day
* if no day in future where warmer temp will appear on ith day set result[i] to 0

temperatures = [85, 97]
result = [1, 0]

temperatures = [88, 80, 76]
result = [0, 0, 0]

temperatures = [76, 76, 88, 85, 82, 90]
result       = [2, 1, 3, 2, 1, 0]

There exists an O(N^2) time complexity solution where you check all other days to find
the day where its hotter than the original day. If it's cooler or stays at the same temp,
you increase day counter by 1 (where day counter is initialized to 0), if its hotter than the original day
then you set result[i] = day counter and move onto the next temperature in the list

right to left traversal
* we know the last temperature's result will always be 0 because there is no temps to the right of it
* we record the last temp as the highest and its index so that we know how many days ahead will be a hotter temp

--  caveat with going from right to left is that we also need to find the closest warmer temperature...
--  we cannot use the global hottest temp as the reference point....

we can use a stack to keep track of which temperatures we visited from right to left

for the stack, I want to preserve descending order...

- bottom of stack is the hottest temp
- top of stack is the coolest temp

-- push temps that are cooler than the top of stack
-- pop top of stack if current temp is hotter than the top (keep on doing this until either stack is empty or you reach a temp on the stack that is hotter)
-- if temp is cooler on top of stack, pop it off and put it in another stack
    -- keep on doing this until stack is empty...

(40, 5)
(38, 1)

'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # non-decreasing order (bottom is hottest, top is coolest)
        # tuple (temp, index)
        stk = []
        res = []

        for i in range(len(temperatures) - 1, -1, -1):
            if len(temperatures) - 1 == i:
                res.append(0)
            else:
                currTemp = stk[-1][0]
                currTempIndex = stk[-1][1]
                while len(stk) > 0 and currTemp <= temperatures[i]:
                    stk.pop()
                    if len(stk) > 0:
                        currTemp = stk[-1][0]
                        currTempIndex = stk[-1][1]

                # no hotter temps
                if len(stk) == 0:
                    res.append(0)
                else:
                    daysAhead = currTempIndex - i
                    res.append(daysAhead)

            stk.append((temperatures[i], i))

        # list is reversed because the original input is processed from right to left
        res.reverse()
        return res
        