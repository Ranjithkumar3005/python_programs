class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        pre=[0]*n
        suf=[0]*n
        sum1=0
        sum2=0
        for i in range(0,n):
            sum1+=nums[i]
            pre[i]=sum1
            sum2+=nums[n-i-1]
            suf[n-i-1]=sum2
        result = [0] * n
        for i in range(n):
            left = nums[i] * i - (pre[i - 1] if i > 0 else 0)
            right = (suf[i + 1] if i < n - 1 else 0) - nums[i] * (n - i - 1)
            print(left,right)
            result[i] = left + right

        return result
        
        
        

s=Solution()
print(s.getSumAbsoluteDifferences( nums = [2,3,5]))