class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        dum1={}
        dum={}
        for i in range(1,a+1):
            if a%i==0:
                dum1[i]=1
        for j in range(1,b+1):
            if b%j==0 and j in dum1:
                dum[j]=1
        print(len(dum))
            
        

s=Solution()
s.commonFactors(a=25,b=30)