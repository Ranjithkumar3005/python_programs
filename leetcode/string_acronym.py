class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        dummy=""
        for i in range(0,len(words)):
            dummy+=words[i][0]
        
        if dummy==s:
            return True
        else:
            return False
    
s=Solution()
print(s.isAcronym(words = ["alice","bob","charlie"], s = "abc"))