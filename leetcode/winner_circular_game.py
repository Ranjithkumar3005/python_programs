class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if k==1:
            return n
        dum=[]
        for i in range(1,n+1):
            dum.append(i)
        c=0
        while len(dum)>1:
            first=dum[0]
            dum.remove(first)
            dum.append(first)
            c+=1
            if c==k-1:
                c=0
                first=dum[0]
                dum.remove(first)
            print(dum)
        print(dum[0])
            

s=Solution()
s.findTheWinner(6,5)
        