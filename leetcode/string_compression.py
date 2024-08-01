class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        c=1
        
        dum=""
        
        for i in range(0,len(word)-1):
            if c==9:
                dum+=str(c)+word[i]
                c=0
            
            if word[i]==word[i+1]:
                c+=1
            else:
                if c!=0:dum+=str(c)+word[i]
                c=1
            
            
        dum+=str(c)+word[len(word)-1]
        print(dum)
        

s=Solution()
s.compressedString(  "aaaaaaaaay")