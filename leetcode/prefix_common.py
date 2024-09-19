class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        h={}
        dum=[]
        for i in range(len(A)):
            h[A[i]]=1
            c=0
            for j in range(0,i+1):
                if B[j] in h:
                    c+=1
            dum.append(c)
        print(dum)
        

s=Solution()
s.findThePrefixCommonArray(A = [1,3,2,4], B = [3,1,2,4])