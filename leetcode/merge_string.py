class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        check=False
        if len(word1)>=len(word2):
            check=True
        s=""
        if check:
            for i in range(0,len(word1)):
                if i<len(word2):
                    s+=word1[i]+word2[i]
                else:
                    s+=word1[i]
        else:
            for i in range(0,len(word2)):
                if i<len(word1):
                    s+=word1[i]+word2[i]
                else:
                    s+=word2[i]
        print(s)       
                
        

s=Solution()
s.mergeAlternately( word1 = "ab", word2 = "pqrs")