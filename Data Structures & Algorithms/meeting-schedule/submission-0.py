"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

'''
Assumptions:
* (0,8) to (8,10) is not considered a schedule conflict
* (0, 6) to (4, 10) is considered a schedule conflict
* for meeting interval (start_i, end_i), start_i < end_i

Task
* return true if all the scheduled meeting times can be attended to without schedule conflict
* false otherwise

Questions:
* are the meeting time intervals sorted? no
* can you have zero meetings as input array? yes
    5  10   15 20 
    *--*    *---*
* -------------------- *
0                      30


If I can write an algorithm to find 1 meeting schedule pair that overlap, then I return false
    - an overlap happens when meeting A and meeting B have:
    => meeting A (as, ae)
    => meeting B (bs, be)
    * either 
        - as <= bs < ae
        - bs <= as < be (not in order)
        - bs < ae < be 
        - as < be < ae  
    * if we sort the intervals, then A and B have an overlap when
        - as <= bs < ae

One way to solve this is to go through each meeting and check it against all other meeting times
    -> if it overlaps, then return false
    -> if not, continue with the next interval
- once all intervals are scanned and no schedule conflicts are found return true

- O(N^2) time complexity

The other way to do this is to sort the meeting intervals by start time which is O(N log N) time if
using merge sort, then do a linear scan

[(0, 30), (30, 45), (55, 85), (100, 126), (2,200)]

             A          B
[(0, 30), (2,200), (30, 45), (55, 85), (100, 126)]

[(5, 25), (5, 35), (45, 125)] returns false because (5,25) and (5,35) overlap


'''

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)
        for i in range(1, len(intervals)):
            if intervals[i-1].start <= intervals[i].start < intervals[i-1].end:
                return False

        return True
