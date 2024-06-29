class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        dum=[]
        for i in range(0,len(matrix[0])):
            dum1=[]
            for j in range(0,len(matrix)):
                dum1.append(matrix[j][i])
            dum.append(dum1)
            dum1=[]
        print(dum)
        
        
s=Solution()
s.transpose(matrix = [[1,2,3]])