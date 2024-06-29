class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max=0
        for i in sentences:
            dum=len(i.split(" "))
            if dum>max:
                max=dum
        print(max)
            
        
        
s=Solution()
s.mostWordsFound(sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"])