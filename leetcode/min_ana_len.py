class Solution(object):
    def minAnagramLength(self, s):
        """
        :type s: str
        :rtype: int
        """

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        h = {}
        for i in s:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        val = h[s[0]]
        for i in range(1, len(s)):
            val = gcd(val, h[s[i]])
        return len(s) // val


s = Solution()
s.minAnagramLength(s="abba")
