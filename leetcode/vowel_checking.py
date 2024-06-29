class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        
        count=0
        for i in range(0,len(words)):
            if (words[i][0]=='a' or words[i][0]=='e' or words[i][0]=='i' or words[i][0]=='o' or words[i][0]=='u') and (words[i][len(words[i])-1]=='a' or words[i][len(words[i])-1]=='e' or words[i][len(words[i])-1]=='i' or words[i][len(words[i])-1]=='o' or words[i][len(words[i])-1]=='u' ):
                count+=1
        return count
s=Solution()
print(s.vowelStrings(words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4))