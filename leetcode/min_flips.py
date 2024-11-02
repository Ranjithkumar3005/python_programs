class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        c = 0
        check = True
        prev = "1"
        for i in target:
            if not check:
                if i != prev:
                    c += 1
                    prev = i
                else:
                    continue
            elif check:
                if i == "0" and check:
                    continue
                elif i == "1":
                    check = False
                    c += 1
        return c
