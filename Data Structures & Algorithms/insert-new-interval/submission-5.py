class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            if newInterval[0] >= intervals[i][0] and newInterval[0] <= intervals[i][1]:
                newInterval[0] = intervals[i][0]
            if newInterval[1] <= intervals[i][1]:
                newInterval[1] = intervals[i][1]
                res.append(newInterval)
                res.extend(intervals[i+1:])
                return res
            if newInterval[0] > intervals[i][0]:
                res.append(intervals[i])
                
        res.append(newInterval)

        return res


            