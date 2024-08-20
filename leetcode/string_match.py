class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dum=set()
        
        for i in range(0,len(words)):
            for j in range(0,len(words)):
                if i!=j and words[i] in words[j]:
                    dum.add(words[i])
        print(dum)
        
        

s=Solution()
s.stringMatching(words = ["mass","as","hero","superhero"])