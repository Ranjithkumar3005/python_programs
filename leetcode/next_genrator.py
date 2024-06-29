class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        h={}
        for i in range(0,len(nums1)):
            h[nums1[i]]=i
        st=True
        for i in range(0,len(nums2)):
            if nums2[i] in h:
                for j in range(i+1,len(nums2)):
                   if nums2[j]>=nums2[i]:
                      nums1[h[nums2[i]]]=nums2[j]
                      st=False
                      break  
                if st:
                    nums1[h[nums2[i]]]=-1
                st=True
        print(nums1)
        
s=Solution()
s.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4])
        
