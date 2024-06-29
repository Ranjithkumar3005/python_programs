
def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j=0
        t=[]
        if m!=0:
            for i in range(0,m):
               t.append(nums1[i])
               if j!=n:   
                   t.append(nums2[j])
                   j+=1
            nums1=t

        else:
            for i in range(0,n):
                t.append(nums2[i])
            nums1=t
        print(nums1)        

merge('self',[2,3,4,5],3,[1,2,3],3)