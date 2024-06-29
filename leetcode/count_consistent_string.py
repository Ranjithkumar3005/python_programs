class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        al=set(allowed)
        count=0
        for i in words:
            if set(i).issubset(al):
                count+=1
        return count
        
s=Solution()
print(s.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))