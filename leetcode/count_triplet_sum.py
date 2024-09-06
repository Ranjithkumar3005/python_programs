class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                for k in range(j+1,n+1):
                    if (i**2)+(j**2)==(k**2):
                        c+=1
        print(c*2)
                        
        
        

s=Solution()
s.countTriples(n=10)