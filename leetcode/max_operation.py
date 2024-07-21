class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        tot=0
        c=0
        check=False
        for i in range(0,len(s)):
            if s[i]=="1":
                c+=1
                check=False
            if s[i]=="0" and not check:
                tot+=c
                check=True
                
        print(tot)
            
s=Solution()
s.maxOperations( s = "1001101")