class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        sum=0
        for i in range(0,len(nums)//2):
            sum+=nums[i]-nums[len(nums)-i-1]
        print(sum)
        

s=Solution()
s.minMoves2( nums =  [1, 3, 5, 8, 10, 12])