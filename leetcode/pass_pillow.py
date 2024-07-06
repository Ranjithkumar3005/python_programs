class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        div = time // (n - 1)
        rem = time % (n - 1)

        if div % 2 == 0:
            return rem + 1

        return n - rem
s=Solution()
print(s.passThePillow(18,38))