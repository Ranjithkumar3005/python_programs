class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        h = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        c = 0
        for i in range(0, len(word)):
            h1 = {}
            j = i
            d = 0
            while j < len(word):
                if word[j] in h:
                    h1[word[j]] = 0
                else:
                    d += 1
                if h == h1 and d == k:
                    c += 1
                if d > k:
                    break
                j += 1
        return c
