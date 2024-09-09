class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        vals=set(nums1+nums2+nums3)
        dum=[]
        for i in vals:
            if (i in nums1 and i in nums2) or (i in nums2 and i in nums3) or (i in nums1 and i in nums3):
                dum.append(i)
        print(dum)
        

s=Solution()
s.twoOutOfThree(nums1 = [3,1], nums2 = [2,3], nums3 = [1,2])