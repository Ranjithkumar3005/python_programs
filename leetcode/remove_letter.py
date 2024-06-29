class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        h={}
        for i in range(0,len(word)):
            if word[i] in h:
                h[word[i]]+=1
            else:
                h[word[i]]=1
        dummy=list(h.values())
        dummy.sort()
        print(dummy)
        print(h)
        count=0
        for i in range(1,len(dummy)):
            if dummy[0]!=dummy[i]:
                count+=1
        
        if count==1 or count==len(dummy)-1:
            if dummy[len(dummy)-1]-1==dummy[len(dummy)-2]:
                return True
            elif dummy[0]-1==0 and dummy[len(dummy)-1]-1==dummy[len(dummy)-2]:
                return True
        if count==0 and dummy[0]-1==0:
            return True
        return False
        
s=Solution()
print(s.equalFrequency("cbccca"))