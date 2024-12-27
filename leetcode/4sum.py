class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        s=set()
        nums=sorted(nums)
        output=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k=j+1
                m=len(nums)-1
                while k<m:
                    sum=nums[i]+nums[j]+nums[k]+nums[m]
                    if sum==target:
                        s.add((nums[i], nums[j], nums[k],nums[m]))
                        k+=1
                        m-=1
                    
                    elif sum<target:
                        k+=1
                    else:
                        m-=1
        output=list(s)
        print(output)
        
          
s=Solution()
s.fourSum(nums = [1,0,-1,0,-2,2], target = 0)