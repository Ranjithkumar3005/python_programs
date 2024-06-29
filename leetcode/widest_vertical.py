class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        dummy=[]
        for i in range(0,len(points)):
            dummy.append(points[i][0])
        dummy.sort()
        value=0
        for i in range(0,len(dummy)-1):
            val=dummy[i+1]-dummy[i]
            if val>value:
                value=val
        print(value)
s=Solution()
s.maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])