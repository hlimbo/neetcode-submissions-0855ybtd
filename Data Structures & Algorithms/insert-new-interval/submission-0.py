# knowns
# - list of intervals is non-overlapping
# - intervals is sorted in ascending order by start_i
# - an interval is shaped as [start_i, end_i]


# input
# newInterval

# output
# return intervals with newInterval added in

# Task
# insert newInterval into intervals such that intervals 
# 1. is still sorted in ascending order by start_i
# 2. intervals does not have any overlapping intervals

# I can merge the overlapping intervals if needed

# 2 intervals overlap given 2 invervals:
# a = [1,3]
# b = [3,7] or [2,7]

# non-overlap
# a = [1,4]
# b = [6,9]

# assuming a is first followed by b
# if a.end_i < b.start_i then no overlap
# if a.end_i >= b.start_i then overlap


# merge mechanic -- its own helper function
# if 2 intervals overlap, then to merge them we do the following
# a = [1,3]
# new_interval = [2, 6]
# a = [min(a.start_i, new_interval.start_i), max(a.end_i, new_interval.end_i)]
# a = [1,6]

# Approach
# create a new intervals list here b/c we may end up with fewer interval items than we start with
# scan through the intervals linearly with the goal of finding a spot to place new interval in
# for each interval
#   if interval.end_i >= new_interval.start_i # overlap
#       interval = mergeIntervals(interval, new_interval)
#       stop as we found the spot to merge new interval in
#   if interval.end_i < new_interval.start_i # no overlap
#       append new_interval after where this interval is located

# for each interval a,b in intervals
#   if interval a overlaps with interval b
#       add the merge of a and b into interval copy
#       remove a and b from intervals
#       stop loop
#   if no overlap
        # add a into intervals_copy

# for each interval a
#   if last interval_copy overlaps with a
#       merge interval_copy with a
#   # if no overlap
#       add a into interval_copy


# above doesn't handle example 1 because we need to see how to merge the interval to the right of it

# time complexity: O(N) where N is number of intervals in list

# Approach - binary search (look for a spot to insert interval in)
# since we know intervals is sorted in asc order by start_i we can check for the conditions
# b is the interval to insert
#   1. a.end_i < b.start_i --> no overlap (this means its in the right side of the array)

# new problem - how to ensure all intervals that are overlapping after the insert are merged?

class Solution:
    def mergeInterval(self, interval_a: List[int], interval_b: List[int]) -> List[int]:
        return [min(interval_a[0], interval_b[0]), max(interval_a[1], interval_b[1])]

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # empty case
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        
        # in between
        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0]:
                intervals.insert(i, newInterval)
                break

        # newInterval is <= than first interval in intervals
        if len(intervals) > 0 and newInterval[1] <= intervals[0][0]:
            intervals.insert(0, newInterval)

        # last interval is smaller than newInterval
        if len(intervals) > 0 and newInterval[0] >= intervals[-1][1]:
            intervals.append(newInterval)

        # tells us where the last non-overlapped interval is located
        last_non_overlapped_interval_index = 0
        intervals_copy = []
        for i in range(len(intervals) - 1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i] = self.mergeInterval(intervals[i], intervals[i+1])
                intervals_copy.append(intervals[i])
                intervals.pop(0)
                intervals.pop(0)
                break
            else: # no overlap
                intervals_copy.append(intervals[i])
                last_non_overlapped_interval_index = i

        # used to check if we need to merge multiple times to reduce the size of
        # the intervals array...
        i = last_non_overlapped_interval_index
        while i < len(intervals):
            interval = intervals[i]
            if intervals_copy[-1][1] >= interval[0]:
                intervals_copy[-1] = self.mergeInterval(intervals_copy[-1], interval)
            elif intervals_copy[-1][1] < interval[0]:
                intervals_copy.append(interval)
            
            i += 1

        return intervals_copy