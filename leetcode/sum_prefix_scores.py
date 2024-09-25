class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        h = {}
        for i in words:
            str1 = ""
            for j in i:
                str1 += j
                if str1 in h:
                    h[str1] += 1
                else:
                    h[str1] = 1
        dum = []
        for i in words:
            c = 0
            str1 = ""
            for j in i:
                str1 += j
                c += h[str1]
            dum.append(c)
        print(dum)


s = Solution()
s.sumPrefixScores(words=["abc", "ab", "bc", "b"])
