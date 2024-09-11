class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dum1=[]
        dum2=[]
        for i in range(0,len(nums)):
            if i%2==0:
                dum1.append(nums[i])
            else:
                dum2.append(nums[i])
        dum1=sorted(dum1)
        dum2=sorted(dum2,reverse=True)
        dum=[]
        i=0
        while i<len(dum1) or i<len(dum2):
            if i<len(dum1):
                dum.append(dum1[i])
            if i<len(dum2):
                dum.append(dum2[i])
            i+=1
        print(dum)
        
        

s=Solution()
s.sortEvenOdd( nums = [4,1,2,3])