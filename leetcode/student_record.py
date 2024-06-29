class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=0
        for i in range(0,len(s)):
            if s[i]=='L':
                l+=1
                if l==3:
                    break
            else:
                l=0
        a=s.count('A')
        if l<3 and a<=2:
            return True
        return False
        
s=Solution()
print(s.checkRecord(s = "LLPPAAALLPLL"))