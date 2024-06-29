class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        dummy=0
        dummy1=0
        for i in range(0,len(p)-1):
            if p[i]=='.':
               dummy+=1
               dummy1+=1
               if p[i+1]=="*":
                   for j in range(dummy,len(s)):
                        dummy+=1
               elif p[i+1]==s[dummy]:
                   dummy+=1
            elif dummy==len(s):
                break          
            elif p[i]!=s[dummy] and p[i+1]=="*":
                dummy1+=1
                continue
            elif p[i]==s[dummy] and p[i+1]=="*":
                dummy1+=1
                for j in range(dummy,len(s)):
                    if p[i]==s[j]:
                        dummy+=1
                    else:
                        break
            elif p[i]==s[dummy]:
                dummy1+=1
                dummy+=1
                if p[i+1]==s[dummy]:
                   dummy1+=1
                   dummy+=1
            elif p[i]=="*":
                dummy1+=1
                continue
            elif p[i+1]=="." or p[i]==".":
                dummy+=1
                dummy1+=1
        dummy1+=1
        print(dummy," ",dummy1)
        if s[len(s)-1]==p[len(p)-1]:
            dummy+=1
        if len(s)!=dummy or dummy1!=len(p):
            return False
        return True
s=Solution()
print(s.isMatch(s ="mississippi",p ="mis*is*ip*."))