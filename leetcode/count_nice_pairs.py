class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h={}
        val=10**9+7
        c=0
        for i in range(0,len(nums)):
            str2=int(str(nums[i])[::-1])
            str1=nums[i]-str2
            if str1 in h:
                c+=h[str1]
            if str1 in h:
                h[str1]+=1
            else:
                h[str1]=1
        print(c%val)
        
        

s=Solution()
s.countNicePairs(nums = [42,11,1,97])