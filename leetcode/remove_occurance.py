class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        while True:
            s=s.replace(part,"",1)
            print(s)
            if part not in s:
                break
        print(s)
        
        

s=Solution()
s.removeOccurrences( s = "aabababa", part = "aba")