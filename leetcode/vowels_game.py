class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h={"a":0,"e":0,"i":0,"o":0,"u":0}
        c=0
        for i in range(0,len(s)):
            if s[i] in h:
                c+=1
        print(c)
        if c==2 or c==0:
            return False
        return True
        
        
s=Solution()
print(s.doesAliceWin( s = "xlsxsrurpi"))