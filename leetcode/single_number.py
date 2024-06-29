class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h={}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        for i in h:
            if h[i]==1:
                return i
        

s=Solution()
print(s.singleNumber(nums = [4,1,2,1,2]))