class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """

        i = 0
        j = 0
        c = 0
        while i < len(str1) or j < len(str2):
            if str1[i] == str2[j]:
                i += 1
                j += 1
            else:
                val = ord(str1[i]) - 97
                val1 = ord(str2[j]) - 97
                if (val == 26 and val1 == 1) or val + 1 == val1:
                    i += 1
                    j += 1
                else:
                    i += 1
        if j == len(str2):
            return True
        return False


s = Solution()
print(s.canMakeSubsequence(str1="abc", str2="ad"))
