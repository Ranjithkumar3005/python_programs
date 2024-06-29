class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        h={}
        
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                h[str(i)+"r"+str(j)]=matrix[i][j]
        for i in h:
            if h[i]==0:
                m=i.split("r")
                for j in range(0,len(matrix[0])):
                    matrix[int(m[0])][j]=0
                
                for j in range(0,len(matrix)):
                    matrix[j][int(m[1])]=0
        print(matrix)
s=Solution()
s.setZeroes([[3,7,2,8,2],[2,2,4,1,8],[0,5,7,6,3],[8,1,0,7,7],[1,3,7,4,1],[6,5,5,6,3],[7,1,0,1,9],[5,4,4,9,7],[2,2,4,1,0],[7,1,1,9,1],[8,0,4,7,6],[7,5,1,2,3],[7,2,5,9,3]])