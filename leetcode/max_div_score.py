class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        h={}
        for i in divisors:
            c=0
            for j in nums:
                if j%i==0:
                    c+=1
            h[i]=c
        max1=max(h.values())
        min1=9999999
        for i in h:
            if h[i]==max1:
                min1=min(min1,i)
        print(min1)
        


s=Solution()
s.maxDivScore(nums = [2,9,15,50], divisors = [5,3,7,2])