class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        dummy=sentence.split(" ")
        print(dummy)
        for i in range(0,len(dummy)):
            if dummy[i][0]!=dummy[i-1][len(dummy[i-1])-1]:
                return False
        return True
        
s=Solution()
print(s.isCircularSentence(sentence = "eetcode"))