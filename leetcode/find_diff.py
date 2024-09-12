class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        arrr1=(set(nums1)-set(nums2))
        arrr2=(set(nums2)-set(nums1))
        return [list(arrr1),list(arrr2)]
        

s=Solution()
print(s.findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))