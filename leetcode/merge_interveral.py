class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
         # If the list of intervals is empty, return an empty list
        if not intervals:
            return []
        
        # Sort intervals by the start time
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # If merged list is empty or there is no overlap, append the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is an overlap, so merge the current interval with the previous one
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
        
        
        

s=Solution()
s.merge(intervals = [[1,4],[0,4]])