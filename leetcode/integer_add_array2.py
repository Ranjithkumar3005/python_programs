class Solution(object):
    def minimumAddedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        
        dum={}
        dum1={}
        for i in range(0,len(nums2)):
            dum={}
            for j in range(0,len(nums1)):
                val=nums2[i]-nums1[j]
                if val not in dum:
                    dum[val]=1
            
            for k in dum:
                if k not in dum1:
                    dum1[k]=1
                else:
                    dum1[k]+=1
        
        dummy1=[]
        dummy2=[]
        for i in dum1:
            if dum1[i]==len(nums2):
                if i>=0:
                    dummy1.append(i)
                else:
                    dummy2.append(i)
        val1=999999999
        if dummy1:
            val2=min(dummy1)
            val1=min(val1,val2)
        
        if dummy2:
            val2=max(dummy2)
            if val1==abs(val2):
                return val2
            val1=min(val1,abs(val2))
        return (val1)
s=Solution()
print(s.minimumAddedInteger( nums1 = [4,20,16,12,8], nums2 = [14,18,10]))