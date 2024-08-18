class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        dum = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i - j in dum:
                    dum[i - j].append(mat[i][j])
                else:
                    dum[i - j] = [mat[i][j]]

        
        for key in dum:
            dum[key].sort(reverse=True)  
            
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = dum[i - j].pop()

        return mat

s = Solution()
result = s.diagonalSort(mat=[[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]])
print(result)
