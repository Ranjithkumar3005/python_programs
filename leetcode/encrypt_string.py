class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        dum=""
        
        for i in range(0,len(s)):
            print(dum)
            if i+k<len(s):
                dum+=s[i+k]
            else:
                val=k-len(s)+i
                dum+=s[val]
                
        print(dum)

s=Solution()
s.getEncryptedString(s = "dart", k = 3)