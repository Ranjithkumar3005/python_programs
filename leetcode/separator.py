class Solution():
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        dummy=[]
        total=[]
        for i in range(0,len(words)):
            dummy=words[i].split(",")
            for j in range(0,len(dummy)):
                total+=dummy[j]
            print(dummy)
        
        print(total)
s=Solution()
s.splitWordsBySeparator(words = ["one,two,three","four,five","six"], separator = ",")