class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        str1=str(bin(n))[2:]
        str1="100001000000010"
        print(str1)
        check=True
        c=0
        max1=0
        for i in range(0,len(str1)):
            if str1[i]=="1" and check:
                check=False
            elif not check and str1[i]=="0":
                c+=1
            elif not check and str1[i]=="1":
                max1=max(max1,c)
                c=0
        print(max1)
        
        

s=Solution()
s.binaryGap(n = 22)