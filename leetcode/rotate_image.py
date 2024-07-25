class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        arr=[]
        n=len(matrix)
        for i in range(0,n):
            str1=[]
            for j in range(0,n):
                str1.append(matrix[j][i])
            arr.append(str1)
        for i in range(0,n):
            for j in range(0,n):
                dummy=arr[i]
                matrix[i][j]=dummy[n-j-1]

s=Solution()
s.rotate( matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])