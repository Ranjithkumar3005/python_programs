nums = [5]
target = 5
value=[-1,-1]
class Solution():
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            if nums[i]==target:
                value[0]=i
                break
        for i in range(len(nums)-1,-1,-1):
            print(i)
            if nums[i]==target:
                value[1]=i
                break
                
        print(value)

s=Solution()
s.searchRange(nums,target)
        