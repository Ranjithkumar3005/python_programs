class Solution(object):
    def subarray(self, array, target):
        dum = []
        for i in range(0, len(array)):
            d = []
            sum1 = 0
            for j in range(i, len(array)):
                d.append(array[j])
                sum1 += array[j]
                if sum1 == target:
                    dum.append(d[:])
        print(dum)

s = Solution()
s.subarray(array=[3, 4, -7, 1, 3, 3, 1, -4], target=7)
