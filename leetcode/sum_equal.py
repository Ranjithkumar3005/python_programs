class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        
        sum1=""
        sum2=""
        tot=""
        
        for i in firstWord:
            val=ord(i)-97
            sum1+=str(val)
        
        for i in secondWord:
            val=ord(i)-97
            sum2+=str(val)
        
        
        for i in targetWord:
            val=ord(i)-97
            tot+=str(val)
        if (int(sum1)+int(sum2))==int(tot):
            return True
        return False
s=Solution()
print(s.isSumEqual( firstWord = "acb", secondWord = "cba", targetWord = "cdb"))