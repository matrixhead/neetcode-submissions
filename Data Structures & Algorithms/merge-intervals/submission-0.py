class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        res = [intervals[0]]
        for inter2 in intervals:
            inter1 = res[-1]
            if inter1[1] >= inter2[0]:
                inter1[1] = max(inter1[1],inter2[1])
            else:
                res.append(inter2)
        
        return res

        