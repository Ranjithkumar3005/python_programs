class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dum=sorted(nums)
        arr=[]
        for i in range(0,len(nums)):
            ind=dum.index(nums[i])
            arr.append(len(dum)-(len(dum)-ind))
        print(arr)
        
        

s=Solution()
s.smallerNumbersThanCurrent(nums = [8,1,2,2,3])