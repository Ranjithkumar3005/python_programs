class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        return max((nums[-1]*nums[-2]*nums[-3]),(nums[0]*nums[1]*nums[-1]))
        
        

s=Solution()
s.maximumProduct([-100,-98,-1,2,3,4])