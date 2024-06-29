class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        seenAlready = []
        for c in s:
            if c not in seenAlready:
                seenAlready.append(c)
            else:
                return c
        

s=Solution()
print(s.repeatedCharacter(s = "abccdddd"))