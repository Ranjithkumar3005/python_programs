class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        x=[]
        y=[]
        for i in range(0,len(words)):
            x+=(words[i].split(separator))
        for i in range(0,len(x)):
            if x[i]!="":
                y.append(x[i])
        return y
        
s=Solution()
print(s.splitWordsBySeparator( words = ["|||"], separator = "|"))