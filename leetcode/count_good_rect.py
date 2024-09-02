class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        h={}
        for i in rectangles:
            min1=min(i[0],i[1])
            if min1 in h:
                h[min1]+=1
            else:
                h[min1]=1
        print(h)
        max1=max(h.keys())
        return h[max1]
        

s=Solution()
print(s.countGoodRectangles(rectangles = [[5,8],[3,9],[5,12],[16,5]]))