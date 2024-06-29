class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        h={}
        dum=[]
        c=0
        h2={}
        d=0
        for i in pattern:
                h2[i]=1
        for i in range(0,len(words)):
            for j in range(0,len(words[i])):
                if words[i][j] not in h:
                    h[words[i][j]]=pattern[j]
                    c+=1
                    d+=1
                else:
                    if h[words[i][j]]==pattern[j]:
                        print(h[words[i][j]]," ",pattern[j]," ",j," ",i)
                        d+=1
            if c==len(h2) and d==len(words[i]):
                dum.append(words[i])
            c=0
            h={}
            d=0
        print(dum)

s=Solution()
s.findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb")