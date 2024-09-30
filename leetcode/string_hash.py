class Solution(object):
    def stringHash(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        val = ""
        for i in range(0, len(s), k):
            tot = 0
            for j in range(i, i + k):
                tot += ord(s[j]) - 97
            tot %= 26
            val += chr(tot + 97)
        print(val)


s = Solution()
s.stringHash(s="abcd", k=2)
