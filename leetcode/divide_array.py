class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        d2=[]
        dum=[nums[0]]
        c=1
        print(nums)
        for i in range(1,len(nums)):
            c+=1
            if nums[i]-nums[i-1]>k and c!=1:
                return []
            if c==3 and nums[i]-nums[i-2]>k:
                print(nums[i],' ',c)
                return []
            
            dum.append(nums[i])
            if c==3:
                d2.append(dum)
                dum=[]
                c=0
        print(d2)
        
s=Solution()
s.divideArray(nums =[1,3,4,8,7,9,3,5,1],k = 2)