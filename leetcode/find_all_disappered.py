class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dum=[]
        h={}
        for i in nums:
            if i not in h:
                h[i]=1
        j=1
        while j<=len(nums):
            if j not in h:
                dum.append(j)
            j+=1
        print(dum)
             
s=Solution()
s.findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1])