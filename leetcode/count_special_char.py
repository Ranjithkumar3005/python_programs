class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        h1={}
        c=0
        
        for i in word:
            if i.islower() and i not in h1:
                if i.upper() in word:
                    c+=1
            
            h1[i]=0
        print(c)
s=Solution()
s.numberOfSpecialChars(word = "AbBCab")