class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        last_alloted = intervals[0]
        res = 0
        for i in range(1,len(intervals)):
            if last_alloted[1] > intervals[i][0]:
                res+=1
            else:
                last_alloted = intervals[i]
        
        return res
