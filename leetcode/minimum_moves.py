class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        sum=0
        for i in range(1,len(nums)):
            sum+=(nums[i-1]-nums[i])*i
        print(sum)
        
s=Solution()
s.minMoves(nums = [1,2,3])