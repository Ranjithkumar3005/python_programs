class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dum=[]
        
        for i in range(0,len(nums),2):
            for j in range(0,nums[i]):
                dum.append(nums[i+1])
        print(dum)
        

s=Solution()
s.decompressRLElist(nums = [1,2,3,4])