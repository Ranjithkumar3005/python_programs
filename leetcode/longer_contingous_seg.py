class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c1=1
        c0=1
        max1=0
        max0=0
        for i in range(0,len(s)-1):
            if s[i]==s[i+1]=="1":
                c1+=1
            else:
              if max1<c1:
                  max1=c1
              c1=1
        if max1<c1:
                  max1=c1
        for i in range(0,len(s)-1):
            if s[i]==s[i+1]=="0":
                c0+=1
            else:
              if max0<c0:
                  max0=c0
              c0=1
        if max0<c0:
                  max0=c0
        print(max0)
        if max1>max0:
            return True
        return False               
        
s=Solution()
print(s.checkZeroOnes("1"))