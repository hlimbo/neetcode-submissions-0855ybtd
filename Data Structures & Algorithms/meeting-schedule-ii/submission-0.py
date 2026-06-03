"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

'''
Assumptions:
* (0,8) and (8,10) is not a conflict at 8
* (2, 10) and (2, 32) is considered a conflict at 2

Task
* find min number of rooms to schedule all meetings without any conflicts

The logic could be after we sort the meeting intervals in asc order by start time...
* if the end of meeting A > start of meeting B, then increase min number of rooms by 1

Base Case:
* if no meetings, then min number of rooms is 0
* if 1 meeting, then min number of rooms is 1

If a time conflict is found, need to check if the other rooms won't have time conflicts with it
* if all rooms have time conflicts, then you need to increase the min number of rooms by 1

data structure to use: 2d array where outer array represents list of rooms
and inner array represents list of intervals that have no time conflict with each other for room i


[(0,20), (1,5), (2, 4), (3,8), (4, 10) ]


Test Cases
- [(0,20), (1,5), (2,4), (3,8), (9,10)] => returns 4
- [(0,20), (1,5), (2,4), (3,8), (1, 5)] => returns 5
- [(4,9)] => returns 1
- [(0,40),(5,10),(15,20)] => returns 2

0 - (0,20)
1 - (1,5), (9,10)
2 - (2,4)
3 - (3,8)

'''

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # base case - 0 or 1 meetings
        if len(intervals) <= 1:
            return len(intervals)

        intervals.sort(key=lambda interval: interval.start)
        rooms = []
        rooms.append([])
        rooms[0].append(intervals[0])

        for i in range(1, len(intervals)):
            needToMakeNewRoom = True
            roomIndexToAddMeetingIn = -1
            # check which room we can put the meeting in so that we don't create more rooms than necessary
            for roomIndex in range(len(rooms)):
                lastMeeting = rooms[roomIndex][-1]
                # no schedule overlap for a given room?
                if intervals[i].start >= lastMeeting.end:
                    needToMakeNewRoom = False
                    roomIndexToAddMeetingIn = roomIndex
                    break

            if needToMakeNewRoom:
                rooms.append([intervals[i]])
            else:
                rooms[roomIndexToAddMeetingIn].append(intervals[i])

        minRooms = len(rooms)
        return minRooms
        