class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        s=s.lower()
        for i in range(0,len(s)-1):
            if s[i]!=s[i+1]:
                c+=1
        print(c)
        
        

s=Solution()
s.countKeyChanges(s = "ab")