class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums=sorted(nums)
        output=99999999
        val=0
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                out=nums[i]+nums[j]+nums[k]
                if out==target:
                    return out
                elif out<target:
                   sum=abs(target-(out))
                   if output>sum:
                       sum=output
                       val=out
                       j+=1
                       
                else:
                    sum=abs(out-target)
                    if output>sum:
                       output=sum
                       val=out
                      
                       k-=1
              
        
        print(val)
        
        

s=Solution()
s.threeSumClosest(nums = [4,0,5,-5,3,3,0,-4,-5], target = -2)