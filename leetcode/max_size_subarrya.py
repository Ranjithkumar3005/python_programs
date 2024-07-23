class Solution(object):
    def minSizeSubarray(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        j=0
        val=99999999
        if target in nums:
            return 1
        for i in range(0,len(nums)):
            tot=nums[i]
            c=1
            if i==len(nums)-1:
                print(i)
                j=0
            else:
                j=i+1
            while True:
                c+=1
                tot+=nums[j]
                if tot>target:
                    break
                if tot==target:
                    if val>c:
                        val=c
                    break
                j+=1
                if j==len(nums):
                    j=0
        if val==99999999:
            return -1
        return val

s=Solution()
print(s.minSizeSubarray( nums = [1,1,1,2,3], target = 4))