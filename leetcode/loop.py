class Solution():
    def func(self,nums,k):
        dum=[0]*k
        
        for i in range(0,len(nums)-1):
            if nums[i]<=nums[i+1]:
                for j in range(nums[i],nums[i+1]+1):
                    dum[j-1]+=1
            else:
                for j in range(nums[i],nums[i+1]-1,-1):
                    dum[j-1]+=1
        max1=max(dum)
        for i in range(0,len(dum)):
            if dum[i]==max1:
                return i+1
    
    
s=Solution()
print(s.func(nums=[2,4,1,3],k=5))