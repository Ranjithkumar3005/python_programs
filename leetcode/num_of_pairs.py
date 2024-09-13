class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        h={}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        c1=0
        c2=0
        for i in h:
            c1+=(h[i]//2)
            c2+=(h[i]%2)
        print([c1,c2])
        
        

s=Solution()
s.numberOfPairs(nums = [1,3,2,1,3,2,2])