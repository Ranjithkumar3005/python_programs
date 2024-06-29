class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        dummy1=""
        dummy2=""
        for i in range(0,len(word1)):
            dummy1+=word1[i]
        for i in range(0,len(word2)):
            dummy2+=word2[i]
        if dummy1==dummy2:
            return True
        return False
        
s=Solution()
s.arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"])