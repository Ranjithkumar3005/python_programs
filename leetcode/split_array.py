class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        h={}
        
        for i in nums:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
                if h[i]>2:
                    return False
        return True
        
        
        

s=Solution()
s.isPossibleToSplit(nums = [1,1,2,2,3,4])