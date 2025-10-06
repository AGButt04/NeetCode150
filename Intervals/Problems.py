# This file has all the problems in the Sliding Window
# section of the NeetCode150 with the explanations.
import heapq

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def canAttendMeetings(intervals):
    for i in range(len(intervals)):
        curr1 = intervals[i]
        for j in range(i + 1, len(intervals)):
            curr2 = intervals[j]

            starting = curr1[1] < curr2[0]
            ending = curr2[1] > curr1[0]

            if starting and ending:
                continue
            else:
                return False

    return True

def insert(intervals, newInterval):
    newIntervals = []

    # iterate through all existing intervals
    for i in range(len(intervals)):
        interval = intervals[i]

        # case 1: newInterval ends before current interval starts (no overlap)
        if newInterval[1] < interval[0]:
            newIntervals.append(newInterval)
            # append rest of intervals as-is and return
            return newIntervals + intervals[i:]

        # case 2: newInterval starts after current interval ends (no overlap)
        elif newInterval[0] > interval[1]:
            newIntervals.append(interval)

        # case 3: intervals overlap → merge them
        else:
            newStart = min(newInterval[0], interval[0])
            newEnd = max(newInterval[1], interval[1])
            newInterval = [newStart, newEnd]

    # add the last merged interval
    newIntervals.append(newInterval)

    # Time Complexity: O(n) for going through the array once
    # Space Complexity: O(n) for storing the new intervals

    return newIntervals

def merge(intervals):
    newIntervals = []
    # sort intervals by starting time
    intervals.sort(key=lambda x: x[0])

    # take the first interval as the starting "overlap candidate"
    overlapping = intervals[0]

    # iterate over the rest
    for i in range(1, len(intervals)):
        currInterval = intervals[i]

        # case 1: overlap exists → merge
        if overlapping[1] >= currInterval[0]:
            newStart = min(currInterval[0], overlapping[0])
            newEnd = max(currInterval[1], overlapping[1])
            overlapping = [newStart, newEnd]
        # case 2: no overlap → save current overlap and reset
        else:
            newIntervals.append(overlapping)
            overlapping = currInterval

    # add the last interval
    newIntervals.append(overlapping)
    # Time Complexity: O(n) for going through the array once
    # Space Complexity: O(n) for storing the new intervals

    return newIntervals


def minMeetingRooms(intervals):
    heap = []
    intervals.sort(key=lambda x: x.start)

    for interval in intervals:
        currEnd = interval.end

        while heap and heap[0] < currEnd:
            heapq.heappop(heap)

        heapq.heappush(heap, currEnd)

    return len(heap)

def eraseOverlapIntervals(intervals):
    minIntervals = 0
    intervals.sort(key=lambda x: x[0])
    overlapper = intervals[0][1]

    for start, end in intervals[1:]:

        if start < overlapper:
            minIntervals += 1
            overlapper = min(overlapper, end)
        else:
            overlapper = end

    return minIntervals

if __name__ == '__main__':
    intervals = [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
    intervals2 = [[1,2],[2,4],[1,4]]
    intervals3 = [[1, 2], [2, 4]]
    # print(minMeetingRooms(intervals))
    print(eraseOverlapIntervals(intervals2))

