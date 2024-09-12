class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot=sum(nums)
        pre=[]
        sum1=0
        for i in nums:
            sum1+=i
            pre.append(sum1)
        c=0
        print(pre)
        for i in range(0,len(pre)-1):
            if pre[i]>=(sum1-pre[i]):
                c+=1
        print(c)
        
        

s=Solution()
s.waysToSplitArray(nums = [10,4,-8,7])