class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=0
        c=0
        check=False
        for i in range(0,len(nums)):
            if nums[i]==1:
                c+=1
                check=True
            elif nums[i]==0:
                if c>max and check:
                    max=c
                c=0
        if c>max and check:
            max=c
        print(max)

s=Solution()
s.findMaxConsecutiveOnes( [0,0])