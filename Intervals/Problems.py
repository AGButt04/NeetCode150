# This file has all the problems in the Sliding Window
# section of the NeetCode150 with the explanations.

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

    return newIntervals

if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(canAttendMeetings(intervals))
