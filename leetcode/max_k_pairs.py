class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums=sorted(nums)
        left=0
        right=len(nums)-1
        c=0
        while left<right:
            sum=nums[left]+nums[right]
            if sum>k:
                right-=1
            elif sum<k:
                left+=1
            else:
                c+=1
                left+=1
                right-=1
        print(c)
        
        

s=Solution()
s.maxOperations(nums = [1,2,3,4], k = 5)