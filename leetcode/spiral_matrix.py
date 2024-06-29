class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        dum=matrix[0]
        i=1
        k=1
        d=1
        j=len(matrix[0])-1
        while True:
            dum.append(matrix[i][j])
            d+=1
            print(dum)
            if i==len(matrix)-k:
                j-=1
            if j==-1:
                k+=1
                j=0
                i-=1
                print(i," ",j)
            if i!=len(matrix)-k:
                i+=1
            if d==len(dum):
                break
s=Solution()
s.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]])