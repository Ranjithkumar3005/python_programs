class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        h1={}
        h2={}
        for i in word1:
            if i in h1:
                h1[i]+=1
            else:
                h1[i]=1
        
        for i in word2:
            if i in h2:
                h2[i]+=1
            else:
                h2[i]=1
        for i in h1:
            if i in h2:
                if h1[i]-h2[i]>3 or h1[i]-h2[i]<-3:
                    return False
            else:
                if h1[i]>3:
                    return False
        for i in h2:
            if i in h1:
                if h2[i]-h1[i]>3 or h2[i]-h1[i]<-3:
                    return False
            else:
                if h2[i]>3:
                    return False
        return True
s=Solution()
print(s.checkAlmostEquivalent(word1 ="aaaa",word2 ="bccb"))