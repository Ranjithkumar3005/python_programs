'''
answer = sum of two areas - overlap area

overlap rectangle coordinates:
cx1 = max(ax1, bx1)
cx2 = min(ax2, bx2)
cy1 = max(ay1, by1)
cy2 = min(ay2, by2)

overlap area = max(0, cx2 - cx1) * max(0, cy2 - cy1)
'''

class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        # Calculate the area of the first rectangle
        area1 = (ax2 - ax1) * (ay2 - ay1)
        
        # Calculate the area of the second rectangle
        area2 = (bx2 - bx1) * (by2 - by1)
        
        sum=area1+area2
        cx1 = max(ax1, bx1)
        cx2 = min(ax2, bx2)
        cy1 = max(ay1, by1)
        cy2 = min(ay2, by2)

        overlap_area = max(0, cx2 - cx1) * max(0, cy2 - cy1)
        
        return sum-overlap_area
        

s=Solution()
print(s.computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2))