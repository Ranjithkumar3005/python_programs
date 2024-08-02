class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1=1
        min2=1
        sum=1
        for i in range(0,len(nums)-1):
              if nums[i]>nums[i+1]:
                  sum+=1
              else:
                  min1=max(min1,sum)
                  sum=1
        min1=max(min1,sum)
        sum=1
        for i in range(0,len(nums)-1):
              if nums[i]<nums[i+1]:
                  sum+=1
              else:
                  min2=max(min2,sum) 
                  sum=1
        min2=max(min2,sum)
        return max(min1,min2)
        

s=Solution()
print(s.longestMonotonicSubarray( nums = [1,4,3,3,2]))