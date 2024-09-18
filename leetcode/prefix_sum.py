class Solution(object):
    def findPrefixScore(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        max1=nums[0]
        conver=[]
        for i in range(0,len(nums)):
            max1=max(max1,nums[i])
            conver.append(nums[i]+max1)
        dum=[0]*len(conver)
        dum[0]=conver[0]
        for i in range(1,len(conver)):
            dum[i]=dum[i-1]+conver[i]
        print(dum)
        
        

s=Solution()
s.findPrefixScore(nums = [2,3,7,5,10])