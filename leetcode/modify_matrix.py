class Solution(object):
    def modifiedMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        h={}
        for i in range(0,len(matrix[0])):
            h[i]=0
            for j in range(0,len(matrix)):
                    if h[i]<matrix[j][i]:
                        h[i]=matrix[j][i]
        print(h)
        for i in range(0,len(matrix[0])):
            for j in range(0,len(matrix)):
                if matrix[j][i]==-1:
                    matrix[j][i]=h[i]
        print(matrix)
s=Solution()
s.modifiedMatrix([[1,2,-1],[4,-1,6],[7,8,9]])