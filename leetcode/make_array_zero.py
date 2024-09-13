class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        c=0
        d=[]
        nums=sorted(nums)
        dum=[]
        for i in nums:
            if i==0:
                continue
            else:
               dum.append(i)
        nums=dum[:]
        print(nums)
        while nums:
            dum=[]
            min1=min(nums)
            for i in nums:
                if (i-min1)!=0:
                    dum.append(i-min1)
            nums=dum[:]
            c+=1
        print(c)
        

s=Solution()
s.minimumOperations(nums = [1,5,0,3,5])