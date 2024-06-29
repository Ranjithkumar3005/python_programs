class Solution(object):
    def countWords(self, words1, words2):
        commonone=[]
        for word in words1 and words2:
            if words1.count(word)==1 and words2.count(word)==1:
                commonone.append(word)
        
        return len(commonone)
        
s=Solution()
print(s.countWords(words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]))