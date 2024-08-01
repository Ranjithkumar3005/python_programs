class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)<3:
            return False
        vol=['a','e','i','o','u','A','E','I','O','U']
        c=0
        v=0
        for i in range(0,len(word)):
            if word[i].isdigit():
                continue
            if word[i] in vol:
                v+=1
                continue
            if (ord(word[i])>=65 and ord(word[i])<=90) or (ord(word[i])>=97 and ord(word[i])<=122):
                c+=1
            else:
                return False 
        if c==0 or v==0:
            return False
        return True
        
s=Solution()
print(s.isValid( word = "234Adas"))