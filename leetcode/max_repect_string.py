class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        count=0
        dummy=word
        while True:
            if sequence.count(dummy)!=0:
                count+=1
                dummy+=word
            else:break
        print(count)
        
        
s=Solution()
s.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba","aaaba")