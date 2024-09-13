class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        h={}
        for i in range(0,len(nums)):
            h[nums[i]]=i
        
        for i in operations:
            nums[h[i[0]]]=i[1]
            h[i[1]]=h[i[0]]
            del h[i[0]]
            
        print(nums)
        
        

s=Solution()
s.arrayChange(nums = [1,2], operations = [[1,3],[2,1],[3,2]])