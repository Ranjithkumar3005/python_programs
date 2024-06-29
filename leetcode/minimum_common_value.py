class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        h={}
        for i in nums1:
            h[i]=1
        for j in nums2:
            if j in h:
                return j
        return -1
        
        
s=Solution()
s.getCommon(nums1 = [1,2,3,6], nums2 = [2,3,4,5])