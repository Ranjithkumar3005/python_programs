class Solution(object):
    def addedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        return min(nums2)-min(nums1)
        
s=Solution()
s.addedInteger( nums1 = [2,6,4], nums2 = [9,7,5])