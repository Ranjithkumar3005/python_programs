class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        max1=-1
        h={}
        for i in arr:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        
        for i in h:
            if i==h[i]:
                max1=max(max1,i)
        print(max1)
        
        
        

s=Solution()
s.findLucky( arr = [2,2,3,4])