class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dum=[]
        dum1=[1]
        dum2=[1]
        
        dum.append(dum1)
        for i in range(1,numRows):
            sum=0
            dum1=[]
            dum1.append(1)
            for j in range(0,len(dum2)-1):
                sum+=dum2[j]+dum2[j+1]
                dum1.append(sum)
                sum=0
            dum1.append(1)
            dum2=dum1
            dum.append(dum1)
        print(dum)
                
        
        
        

s=Solution()
s.generate(5)