class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1=[]
        num2=[]
        for i in nums:
            if i%2==0:
                num1.append(i)
            else:
                num2.append(i)
        final=[]
        for i in range(0,len(num1)):
            final.append(num1[i])
            final.append(num2[i])
        print(final)
        
        

s=Solution()
s.sortArrayByParityII(nums = [4,2,5,7])