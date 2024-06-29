class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        h={}
        for i in range(0,len(magazine)):
            if magazine[i] in h:
                h[magazine[i]]+=1
            else:
                h[magazine[i]]=1
        
        for i in range(0,len(ransomNote)):
            if ransomNote[i] not in h:
                return False
            else:
                h[ransomNote[i]]-=1
            if h[ransomNote[i]]==-1:
                return False
        
        return True
s=Solution()
s.canConstruct(ransomNote = "aaa", magazine = "aabbb")