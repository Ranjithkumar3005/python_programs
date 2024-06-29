class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        strs=""
        for i in words:
            strs+=i
            if s==strs:
                return True
        return False
s=Solution()
print(s.isPrefixString(s = "iloveleetcode", words = ["i","love","leetcode","apples"]))