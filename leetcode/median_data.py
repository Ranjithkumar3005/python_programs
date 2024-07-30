class MedianFinder(object):

    def __init__(self):
        self.dum=[]

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.dum.append(num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        self.dum=sorted(self.dum)
        temp=len(self.dum)
        if temp%2!=0:
            return self.dum[temp//2]
        return (self.dum[temp//2]+self.dum[(temp//2)-1])/2


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
# obj.addNum(3)
# obj.addNum(5)
param_2 = obj.findMedian()
print(param_2)