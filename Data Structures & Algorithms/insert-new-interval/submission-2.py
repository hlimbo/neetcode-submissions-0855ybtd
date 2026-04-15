'''
    -- knowns --
* intervals is sorted in ascending order by start_i
* interval is shaped as = [start, end]
* I can assume start < end
* list of intervals given are ALL non-overlapping
    e.g. [a1, b1] < [a2, b2] where b1 < a2

Task
* add a newInterval into intervals such that intervals STILL SORTED IN ASC ORDER BY START_I
* also make sure intervals have no overlapping intervals
* may need to merge overlapping intervals needed

Examples

intervals [[3,5],[6,7], [9,10]], newInterval = [1,2]
answer = [[1,2], [3,5],[6,7], [9,10]]

intervals [[3,5],[6,7], [9,10]], newInterval = [11, 20]
answer = [[3,5],[6,7], [9,10], [11, 20]]

intervals [3,5], [6,7], [9,10], newInterval = [1, 20]
answer = [1,20]

High Level approaches:
1. linear scan
2. binary search?
3. 2 pointer?
    - leftIndex = 0, rightIndex = len(intervals)
    - check if left side intervals overlap with new Interval
        scan left 2 right
            - if currInterval.end < newInterval.start
                - leftIndex += 1
    - check if right side intervals overlap with new Interval
        scan right 2 left
            - if currInterval.start > newInterval.end
                - rightIndex -= 1

    # non overlapping intervals left side
    from 0 to left index exclusive in intervals
        add all intervals into new intervals copy

    * left and right indices represent the range in which overlaps may occur
    -- overlaps
    from left index to right index inclusive in intervals
        * if currInterval.start <= newInterval.start <= currInterval.end
            newInterval = [min(currInterval.start, newInterval.start), max(currInterval.end, newInterval.end)]
        else:
            add currInterval to intervals copy

    add newInterval to end of intervals copy

    # non overlapping intervals right side
    from right index to end of intervals
        add all intervals into intervals copy

Sub problems:
1. look for the index where newInterval can be inserted in intervals
    -- scan from left to right
        - if currInterval.end < newInterval.start
            - nonOverlapIndex is increased by 1
2. before inserting, check if the spot inserting overlaps with any adjacent intervals
'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        leftIndex = 0
        rightIndex = len(intervals) - 1

        while leftIndex < len(intervals) and intervals[leftIndex][1] < newInterval[0]:
            leftIndex += 1
        
        while rightIndex > -1 and intervals[rightIndex][0] > newInterval[1]:
            rightIndex -= 1

        intervalsCopy = []
        for l in range(0, leftIndex):
            intervalsCopy.append(intervals[l])

        # maybe overlapping items
        for i in range(leftIndex, rightIndex + 1):
            if intervals[i][1] >= newInterval[0]:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            else:
                intervalsCopy.append(intervals[i])

        # add new interval with merges maybe included
        intervalsCopy.append(newInterval)

        for r in range(rightIndex + 1, len(intervals)):
            intervalsCopy.append(intervals[r])

        return intervalsCopy