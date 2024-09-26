class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        c = 0

        for i in range(low, high + 1):
            str1 = str(i)
            if len(str1) % 2 != 0:
                continue
            else:
                mid = len(str1) // 2
                sum1 = 0
                sum2 = 0
                for j in range(mid):
                    sum1 += int(str1[j])
                    sum2 += int(str1[j + mid])
                if sum1 == sum2:
                    c += 1
        print(c)


s = Solution()
s.countSymmetricIntegers(low=1200, high=1230)
