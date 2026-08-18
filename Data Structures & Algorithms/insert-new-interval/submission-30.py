class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        
        # Phase 1: Append all intervals that end strictly before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # we found the start of the newInterval
        if i<n: 
            newInterval[0] = min(newInterval[0], intervals[i][0])
            
        # Phase 2: Merge all overlapping intervals into newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        
        # Phase 3: Append the remaining intervals that start strictly after newInterval ends
        res.extend(intervals[i:])
            
        return res