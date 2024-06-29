class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1=sorted(nums)
        return ((nums1[len(nums1)-1]*nums1[len(nums1)-2])-(nums1[0]*nums1[1]))
        
        
        
s=Solution()
print(s.maxProductDifference([4,2,5,9,7,4,8]))