class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        h={}
        for i in nums1:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
        d=[]
        for i in nums2:
            if i in h and h[i]!=0:
                h[i]-=1
                d.append(i)
        print(d)
        
        
s=Solution()
s.intersect(nums1 = [1,2,2,1], nums2 = [2,2])