'''
- interval = [start_i, end_i]
- intervals sorted in asc order by start_i

inputs:
- list of intervals sorted in asc order by start_i
- interval to insert [start_i, end_i] => newInterval

output:
* return intervals after inserting new interval

Rules
1. intervals remains sorted in ascending order after inserting newInterval
2. intervals has no overlapping intervals
3. can merge overlapping intervals IF NEEDED


examples
[1,2] [3,4] are non-overlapping

[1,5] [2,6] are overlapping


intervals
[] 
[1,5]
output:
[[1,5]]

[[3,10]]
[12,20]
output
[[3,10],[12,20]]

[[3,10]]
[1,2]
output
[[1,2],[3,10]]

[[3,10]]
[1,4]
output
[[1,10]]

[[3,10]]
[8,12]
output
[[3,12]]

[[5,25]]
[8,10]
output
[[5,25]]

Two intervals A and B overlap if
A = new interval
B = interval in intervals list

B.end >= A.start or B.start <= A.start <= A.end <= B.end

possibilities
* B.start <= A.start <= B.end <= A.end
* A.start <= B.start <= A.end <= B.end
* A.start <= B.start <= B.end <= A.end
* B.start <= A.start <= A.end <= B.end

^ Overlapping conditions

Condition to insert?
* if A.start > B.end -- insert last (if on last interval)
* if A.end < B.start -- insert first (if on first interval)
* if A.start > B.end and A.end < (B+1).start -- insert in  middle (if in middle interval)

Build a new intervals list where we compare the current interval in list with new interval

set pendingInterval = new interval

* if pendingInterval overlaps with current interval
    - merge the 2 intervals together and store them in a temp variable called pendingInterval
    - go to the next interval to compare against the pendingInterval with
* if pendingInterval does not overlap with current interval
    - if pendingInterval.end < current interval.start
        - insert pendingInterval to new list
        - insert current interval to list
        - mark as inserted so the algorithm can insert all the intervals from the old list into the new list
    - else
        - insert current interval to list

Time complexity:
O(N) where N is number of intervals in list

Space complexity:
O(N) as I'm making a new list to return
'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newList = []
        pendingInterval = newInterval
        isPendingIntervalInserted = False
        i = 0
        while not isPendingIntervalInserted and i < len(intervals):
            currentInterval = intervals[i]
            doesOverlap = pendingInterval[0] <= currentInterval[0] <= currentInterval[1] <= pendingInterval[1] or pendingInterval[0] <= currentInterval[0] <= pendingInterval[1] <= currentInterval[1] or currentInterval[0] <= pendingInterval[0] <= pendingInterval[1] <= currentInterval[1] or currentInterval[0] <= pendingInterval[0] <= currentInterval[1] <= pendingInterval[1] 

            if doesOverlap:
                # merge the 2 intervals together
                pendingInterval = [min(pendingInterval[0], currentInterval[0]), max(pendingInterval[1], currentInterval[1])]
            else:
                # check for insert conditions
                if pendingInterval[1] < currentInterval[0]:
                    newList.append(pendingInterval)
                    newList.append(currentInterval)
                    isPendingIntervalInserted = True
                else:
                    newList.append(currentInterval)

            i += 1

        # insert remaining intervals
        while i < len(intervals):
            newList.append(intervals[i])
            i += 1

        # add to the last spot in the new list
        if isPendingIntervalInserted == False:
            newList.append(pendingInterval)

        return newList

        