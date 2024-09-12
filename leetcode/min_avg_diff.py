class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre=[]
        suf=[]
        sum1=0
        sum2=0
        for i in range(0,len(nums)):
            sum1+=nums[i]
            pre.append(sum1//(i+1))
        
        num1=nums[::-1]
        
        for j in range(0,len(num1)-1):
            sum2+=num1[j]
            suf.append(sum2//(j+1))
        suf=suf[::-1]
        suf.append(0)
        min1=99999999
        ind=0
        for i in range(0,len(pre)):
            val=abs(pre[i]-suf[i])
            if min1>val:
                min1=val
                ind=i
        print(ind)
        
        

s=Solution()
s.minimumAverageDifference(nums = [2,5,3,9,5,3])