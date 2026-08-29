class Solution:
    def partitionLabels(self, s: str) -> List[int]:  # 感觉像一道合并区间的题目
        bucket = {}
        n = len(s)
        for i in range(n):
            if s[i] in bucket:
                bucket[s[i]][1] = i
            else:
                bucket[s[i]] = [i,i]
        intervals = []
        output = [0]
        for i in bucket:
            intervals.append(bucket[i])
        right = intervals[0][1]
        left = intervals[0][0]
        n = len(intervals)
        for i in range(n):
            if intervals[i][0] < right:               
                if intervals[i][1] > right:
                    right = intervals[i][1]
            else:
                if output[0] == 0:
                    output[-1] = intervals[i][0]
                else:
                    output.append(right - left + 1)
                left = intervals[i][0]
                right = intervals[i][1]
        if output[0] == 0:
            output[-1] = right - left + 1
        else:
            output.append(right - left + 1)
        return output
        
