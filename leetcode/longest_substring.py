class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        dummy = 0
        dummycharacter = ""
        for i in range(0, len(s)):
            if s[i] not in dummycharacter:
                count += 1
                print(count)
                dummycharacter += " " + s[i]
                print(dummycharacter)
                if dummy < count:
                    dummy = count
            else:
                count = 1
                dummycharacter += " " + s[i]
