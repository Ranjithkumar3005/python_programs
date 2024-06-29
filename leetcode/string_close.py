class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        h1={}
        if len(word1)!=len(word2):
            return False
        h2={}
        for i in range(0,len(word1)):
            if word1[i] in h1:
                h1[word1[i]]+=1
            else:
                h1[word1[i]]=1
            if word2[i] in h2:
                h2[word2[i]]+=1
            else:
                h2[word2[i]]=1
        for i in h1:
            if i not in h2:
                return False
        dum1=sorted(list(h1.values()))
        dum2=sorted(list(h2.values()))
        if dum1==dum2:
            return True
        return False
        
s=Solution()
print(s.closeStrings(word1 = "uau", word2 = "ssx"))