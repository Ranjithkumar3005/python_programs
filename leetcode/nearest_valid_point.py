class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        h={}
        
        for i in range(0,len(points)):
            if points[i][0]==x or points[i][1]==y:
                val=abs(x - points[i][0]) + abs(y - points[i][1])
                if val not in h:
                    h[val]=i
        if not h:
            return -1
        min1=sorted(h.items())
        print(min1[0][1])
        
        

s=Solution()
s.nearestValidPoint( x = 3, y = 4, points = [[2,3]])