class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum1=0
        sum2=0
        
        for i in range(0,len(mat)):
            sum1+=mat[i][i]
            sum2+=mat[i][len(mat)-i-1]
        
        if len(mat)%2!=0:
            return sum1+sum2-mat[len(mat)//2][len(mat)//2]
        return sum1+sum2
        
        

s=Solution()
print(s.diagonalSum(mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))