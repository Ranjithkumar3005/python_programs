class Solution(object):
    def valueAfterKSeconds(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dum=[1]*n
        
        for i in range(0,k):
            val=dum[0]
            c=1
            while c<n:
                val+=dum[c]
                dum[c]=val
                c+=1
            
        print((dum[n-1])%1000000007)

s=Solution()
s.valueAfterKSeconds( n = 5, k = 1000)