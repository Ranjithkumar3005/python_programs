class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        dummy=[]
        for i in range(0,len(words)):
            if x in words[i]:
                dummy.append(i)
                
        return dummy
    
    
s=Solution()
print(s.findWordsContaining(words = ["abc","bcd","aaaa","cbc"], x = "z"))