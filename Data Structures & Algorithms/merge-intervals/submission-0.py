'''
overlapping means the end of interval A is <= than the start of interval B
[1,2] [2,3] overlap
[1,4] [3,8] overlap
[1,6] [9, 22] non-overlap

Input
* array of intervals
* an interval is defined as [start_i, end_i]

Output:
* can return array of intervals IN ANY ORDER

Questions
* will the intervals be sorted in ascending order by the start number? No b/c problem statement didn't specify
[[6,7], [1,3], [1,5]]


Brainstorming
1. sort intervals in descending order using python sort function
    - aside: to make it harder, if you don't have a sort function, how would you sort them?
2. for each interval starting from beginning, check if adjacent interval overlaps
    for the overlap case:
    by checking the following:
        intervalA.end <= intervalB.start
    merge operation
        new interval = [min(intervalA.start, intervalB.start), max(intervalA.end, intervalB.end)]
    for not overlap case:
    * place intervalA in a new intervals list
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # descending order by start value of interval
        # the tiebreaker if both start's are the same would be the end value of the interval
        intervals.sort(key=lambda interval: (interval[0], interval[1]), reverse=True)

        newIntervals = []
        newIntervals.append(intervals.pop())
        while len(intervals) > 0:
            # overlap?
            if newIntervals[-1][1] >= intervals[-1][0]:
                # merge
                newIntervals[-1] = [min(newIntervals[-1][0], intervals[-1][0]), max(newIntervals[-1][1], intervals[-1][1])]
                intervals.pop()
            # no overlap
            else:
                newIntervals.append(intervals.pop())

        return newIntervals
        