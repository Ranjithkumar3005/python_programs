class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in words:
            if i==i[::-1]:
                return i
        return ""
        
        
        
s=Solution()
print(s.firstPalindrome(words = ["abc","car","ada","racecar","cool"]))