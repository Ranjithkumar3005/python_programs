class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        num=str(num)
        odd, even = [], []
        arr = [int(i) for i in str(num)]
        for i in arr:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        odd.sort()
        even.sort()
        res = 0
        for i in range(len(num)):
            if arr[i] % 2 == 0:
                res = res*10 + even.pop()
            else:
                res = res*10 + odd.pop()
        return res

s=Solution()
print(s.largestInteger(num = 65875))