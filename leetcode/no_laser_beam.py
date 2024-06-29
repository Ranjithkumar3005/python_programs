class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        sum=0
        n1=0
        dum=[]
        for i in range(0,len(bank)):
            for j in bank[i]:
                if j=="1":
                    n1+=1
            if n1!=0:
                dum.append(n1)
            n1=0
        print(dum)
        if dum==[] or len(dum)==1:
            return 0
        for i in range(0,len(dum)-1):
            sum+=dum[i]*dum[i+1]
        return sum
                    
s=Solution()
s.numberOfBeams(bank = ["011001","000000","010100","001000"])