class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        h1={}
        c=0
        h={}
        for i in word:
            if i.isupper():
                h1[i]=0
            else:
             if i in h:
                h[i]+=1
             else:
                 h[i]=1
        for i in word:
            if i.islower():
                if i.upper() not in h1:
                    continue
                if i in h:
                  h[i]-=1
            elif i.lower() in h and h[i.lower()]==0:
                h[i.lower()]-=1
                c+=1
            else:
                if i.lower() in h:
                 del h[i.lower()]
            
        print(c)
s=Solution()
s.numberOfSpecialChars(word = "dcbCC")