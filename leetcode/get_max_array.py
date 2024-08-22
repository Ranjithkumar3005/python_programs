class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        
        nums=[0]*(n+1)
        nums[1]=1
        i=1
        d=2
        while True:
            nums[2 * i] = nums[i]
            d+=1
            if d==n+1:
                break
            nums[2 * i + 1] = nums[i] + nums[i + 1]
            d+=1
            if d==n+1:
                break
            i+=1
        return max(nums)

s=Solution()
s.getMaximumGenerated(n=7)