class Solution(object):
    def shiftZeros(self, nums):
        dum1=[]
        dum2=[]
        
        for i in nums:
            if i==0:
                dum1.append(0)
            else:
                dum2.append(i)
        for i in dum1:
            dum2.append(i)
        print(dum2)
        
        
        

s=Solution()
s.shiftZeros([0, 1, 0, 3, 12])