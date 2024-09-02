class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        h={}
        
        for i in range(lowLimit,highLimit+1):
            t=i
            if i>=10:
                t=0
                dum=list(str(i))
                for j in dum:
                    t+=int(j)
                    
            if t in h:
                h[t]+=1
            else:
                h[t]=1
        print(max(h.values()))
                    
        
        

s=Solution()
s.countBalls(lowLimit = 19, highLimit = 28)