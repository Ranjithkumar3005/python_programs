class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dum=[]
        h={}
        for i in nums:
            if i in h:
                dum.append(i)
            else:
                h[i]=1
        print(dum)
        

s=Solution()
s.findDuplicates(nums = [4,3,2,7,8,2,3,1])