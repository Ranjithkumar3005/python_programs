class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(1,n+1):
            if(self.check(n,i)):
                return i
        return -1
    
    def check(self,n,n1):
        sum=0
        sum1=0
        for i in range(1,n1+1):           
            sum+=i
            
        for i in range(n,n1-1,-1):
            sum1+=i
        if sum==sum1:
            return True
     
            

s=Solution()
print(s.pivotInteger(4))