class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums=sorted(nums,reverse=True)
        return nums[k-1]
        
        

s=Solution()
s.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4)