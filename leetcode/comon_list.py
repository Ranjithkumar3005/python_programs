class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dummy=[]
        count=0
        for i in range(0,len(nums1)):
            if nums1[i] in nums2:
                count+=1
        dummy.append(count)
        count=0
        for i in range(0,len(nums2)):
            if nums2[i] in nums1:
                count+=1
        dummy.append(count)
        print(dummy)

s=Solution()
s.findIntersectionValues(nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6])