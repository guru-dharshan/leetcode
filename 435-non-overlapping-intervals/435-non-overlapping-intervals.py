class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda p: p[1])
        c=0
        value=intervals[0][1]
        for i in range(1,len(intervals)):
            
            if value > intervals[i][0] and  value<= intervals[i][1]:
                c=c+1
            else:
                value=intervals[i][1]
        return c
                
        