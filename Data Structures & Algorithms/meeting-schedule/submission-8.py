"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x : x.end)
        last_alloted = intervals[0]
        for i in range(1,len(intervals)):
            if last_alloted.end > intervals[i].start:
                return False
            last_alloted = intervals[i]
        
        return  True
