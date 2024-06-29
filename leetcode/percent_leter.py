import math
class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        return math.floor((s.count(letter)/len(s))*100)
        
s=Solution()
print(s.percentageLetter(s = "foobar", letter = "k"))