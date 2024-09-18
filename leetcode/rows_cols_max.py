class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        h={}
        
        for i in range(0,len(mat)):
            c=0
            for j in mat[i]:
                if j==1:
                    c+=1
            h[i]=c
        max1=max(h.values())
        dum=[]
        for i in h:
            if h[i]==max1:
                dum.append(i)
        dum=sorted(dum)
        return [dum[0],max1]        


s=Solution()
print(s.rowAndMaximumOnes(mat = [[0,1],[1,0]]))