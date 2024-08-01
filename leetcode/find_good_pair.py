class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if nums1[i]%(nums2[j]*k)==0:
                    c+=1
        print(c)

s=Solution()
s.numberOfPairs( nums1 = [1,3,4], nums2 = [1,3,4], k = 1)