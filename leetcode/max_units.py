class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        h={}
        
        for i in boxTypes:
            if i[1] in h:
                h[i[1]]+=i[0]
            else:
                h[i[1]]=i[0]
        sorte=sorted(h,reverse=True)
        tot=0
        for i in sorte:
            print(truckSize,tot)
            if truckSize==0:
                break
            if h[i]>truckSize:
                tot+=(truckSize*i)
                truckSize=0
            else:
               tot+=(h[i]*i)
               truckSize-=h[i]
            
        print(tot)
        
        

s=Solution()
s.maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10)