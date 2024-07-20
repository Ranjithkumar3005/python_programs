class Solution(object):
    def minimumAddedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dum=99999999
        min2=min(nums2)
        for i in range(0,len(nums1)):
            temp1=nums1[i]
            nums1[i]=0
            for j in range(i+1,len(nums1)):
                temp2=nums1[j]
                nums1[j]=0
                tot=min2-min(nums1)
                if tot<dum:
                    dum=tot
                nums1[j]=temp2
                
        print(dum)
        
        

s=Solution()
s.minimumAddedInteger( nums1 = [4,20,16,12,8], nums2 = [14,18,10])