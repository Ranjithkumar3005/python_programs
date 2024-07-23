class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1=0
        
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    tot=(nums[i]-nums[j])*nums[k]
                    if tot>max1:
                        max1=tot
        print(max1)
        
        
s=Solution()
s.maximumTripletValue(nums = [1,2,3])