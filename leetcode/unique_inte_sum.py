class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dum=[]
        if n%2!=0:
            dum.append(0)
            
        for i in range(1,(n//2)+1):
            dum.append(i)
            dum.append(i*(-1))
        print(dum)
        

s=Solution()
s.sumZero(n = 4)