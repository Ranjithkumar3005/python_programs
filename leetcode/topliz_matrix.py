class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix)-1,0,-1):
            for j in range(len(matrix[0])-1,0,-1):
                if matrix[i][j]!=matrix[i-1][j-1]:
                    return False
        return True
        
        

s=Solution()
print(s.isToeplitzMatrix(matrix = [[1,2],[2,2]]))