class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        h={}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        for  i in h:
            if h[i]%2!=0:
                return False
        return True
        
        

s=Solution()
s.divideArray(nums = [3,2,3,2,2,2])