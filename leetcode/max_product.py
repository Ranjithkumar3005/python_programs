class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums1=sorted(nums)
        len1=len(nums)
        total=(nums1[len1-1]-1)*(nums1[len1-2]-1)
        print(total)
        
s=Solution()
s.maxProduct([1,5,4,5])