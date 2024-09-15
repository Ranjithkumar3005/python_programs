class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        h={}
        for i in range(0,len(intervals)):
            h[intervals[i][0]]=i
        dum=[]
        for i in intervals:
            if i[1] in h:
                dum.append(h[i[1]])
            else:
                dum.append(-1)
        print(dum)

s=Solution()
s.findRightInterval(intervals = [[4,5],[2,3],[1,2]])