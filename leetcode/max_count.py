class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        banned=set(banned)
        sum=0
        c=0
        for i in range(1,n+1):
            if i in banned:
                continue
            sum+=i
            if sum>maxSum:
                break
            c+=1
        print(c)

s=Solution()
s.maxCount(banned = [1,6,5], n = 5, maxSum = 6)