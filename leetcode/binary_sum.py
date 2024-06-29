class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        sum=0
        count=0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                sum+=nums[j]
                if sum==goal:
                    count+=1 
                if sum>goal:
                    break
            sum=0
        print(count)
        
        
s=Solution()
s.numSubarraysWithSum( nums = [0,0,0,0,0], goal = 0)