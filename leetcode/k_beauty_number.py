class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        c=0
        dum=str(num)
        if len(dum)==k==1:
            return num
        for i in range(0,len(dum)):
            if int(dum[i:i+k-1])!=0 and num%int(dum[i:i+k])==0:
                c+=1
        print(c)
            
        
s=Solution()
print(s.divisorSubstrings(num = 42,k=1))