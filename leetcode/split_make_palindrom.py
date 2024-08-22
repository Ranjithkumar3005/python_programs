class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        if len(a)==1:
            return True
        
        for i in range(1,len(a)):
            apre=a[:i]
            asuf=a[i:]
            bpre=b[:i]
            bsuf=b[i:]
            con1=apre+bsuf
            if con1==con1[::-1]:
                return True
            con2=bpre+asuf
            if con2==con2[::-1]:
                return True
        return False
        
        

s=Solution()
print(s.checkPalindromeFormation(a = "ulacfd", b = "jizalu"))