class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        total=0
        dummy=0
        for i in range(1,n+1):
            dummy+=1
            total+=dummy
            print(dummy)
            if i%7==0:
                dummy-=6
        
        print(total)
            
            
s=Solution()
s.totalMoney(20)