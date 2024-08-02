class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        c=0
        
        for i in range(0,len(words)):
            val=words[i]
            len1=len(val)
            for j in range(i+1,len(words)):
                if words[j][0:len1]==val and words[j][len(words[j])-len1:]==val:
                    c+=1
        print(c)
        
        

s=Solution()
s.countPrefixSuffixPairs(words = ["a","aba","ababa","aa"])