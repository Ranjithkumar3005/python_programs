class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        num1=num
        num=str(num)
        c=0
        
        for i in range(0,len(num)-k+1):
            val=int(num[i:i+k])
            if val!=0 and num1%val==0:
                c+=1
        print(c)
        

s=Solution()
s.divisorSubstrings(num = 430043, k = 2)