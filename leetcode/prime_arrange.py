class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        num=0
        
        for i in range(2,n+1):
            c=0
            for j in range(2,i):
                if i%j==0:
                    c+=1
                    break
            if c==0:
                num+=1
        num1=n-num
        tot=0
        val1=1
        val2=1
        for i in range(num,0,-1):
            val1*=i
        
        for i in range(num1,0,-1):
            val2*=i
        print(val1)
        print(val1*val2)

s=Solution()
s.numPrimeArrangements(n = 5)