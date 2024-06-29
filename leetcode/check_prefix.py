class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        dummy=sentence.split(" ")
        for i in range(0,len(dummy)):
            if dummy[i][0:len(searchWord)]==searchWord:
                return i+1
        return -1
        
        
        
s=Solution()
print(s.isPrefixOfWord( sentence = "this problem is an easy problem", searchWord = "pro"))