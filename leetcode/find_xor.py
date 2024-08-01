class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h={}
        c=[]
        for i in nums:
            if i in h:
                c.append(i)
                
            h[i]=0
        if c==[]:
            return 0
        if len(c)==1:
            return c[0]
        val=c[0]
        for i in range(1,len(c)):
            val=val^c[i]
        print(val)
        
        
        

s=Solution()
s.duplicateNumbersXOR(nums = [1,2,2,1])