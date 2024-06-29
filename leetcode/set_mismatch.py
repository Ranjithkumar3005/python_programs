class Solution(object):
    def findErrorNums(self, nums):
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
        
        dum1=0
        dum2=0
        for i in range(1,len(nums)+1):
            if i not in h:
                dum1=i
                continue
            if h[i]==2:
                dum2=i
        dum3=[]
        dum3.append(dum2)
        dum3.append(dum1)
        print(dum3)
        

s=Solution()
s.findErrorNums( nums = [2,2])