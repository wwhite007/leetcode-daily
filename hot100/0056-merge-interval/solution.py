class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() #这里默认按照每个区间的左端点进行排序。
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i]) #不重合
            else:
                res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]
        return res
        
