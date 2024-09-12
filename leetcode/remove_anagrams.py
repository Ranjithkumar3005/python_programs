class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        val=words[0]
        h1={}
        dum=[val]
        for i in val:
            if i in h1:
                h1[i]+=1
            else:
               h1[i]=1
        for i in range(1,len(words)):
            h2={}
            for j in words[i]:
                if j in h2:
                    h2[j]+=1
                else:
                    h2[j]=1
            if h1!=h2:
                dum.append(words[i])
                h1=h2
        print(dum)
        
        

s=Solution()
s.removeAnagrams(words = ["abba","baba","bbaa","cd","cd"])