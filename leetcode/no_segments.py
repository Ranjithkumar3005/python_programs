class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=s.split(" ")
        dummy=[e for e in m if e not in ('')]
        return len(dummy)
        
s=Solution()
print(s.countSegments( s = "Hello   mr"))