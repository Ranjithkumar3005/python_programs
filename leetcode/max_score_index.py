class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c0=nums.count(0)
        c1=len(nums)-c0
        vals=[]
        vals.append(c1)
        a=0
        for i in nums:
            if i==0:
                c0-=1
                a+=1
                vals.append(a+c1)
            elif i==1:
                c1-=1
                vals.append(a+c1)
        dum=[]
        max1=max(vals)
        for i in range(0,len(vals)):
            if vals[i]==max1:
                dum.append(i)
        print(dum)

s=Solution()
s.maxScoreIndices( nums = [0,0,1,0])