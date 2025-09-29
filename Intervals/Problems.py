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

if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(canAttendMeetings(intervals))
