class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h={}
        for i in nums:
            if i>0:
                h[i]=1
        i=1
        while i!=100001:
            if i not in h:
                return i
            i+=1
                

s=Solution()
print(s.firstMissingPositive(nums = [3,4,-1,1]))