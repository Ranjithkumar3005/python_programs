class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=1
        max=1
        for i in range(0,len(s)-1):
            if s[i]==s[i+1]:
                count+=1
                if i==len(s)-2 and  max<count:
                   max=count
            else:
                if max<count:
                    max=count
                count=1
        return max
        
        
        
s=Solution()
print(s.maxPower("abbcceeeffgkllnnoooppqqrrssttuuvvwwyzz"))