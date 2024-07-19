class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        num=0
        dum1={}
        for i in range(0,len(matrix)):
            dum=min(matrix[i])
            dum1[dum]=0
        max1=0
        print(dum1)
        d=[]
        for i in range(0,len(matrix[0])):
            for j in range(0,len(matrix)):
                if matrix[j][i]>max1:
                    max1=matrix[j][i]
            if max1 in dum1:
                d.append(max1)
            max1=0
        return d
                    
        
        

s=Solution()
print(s.luckyNumbers(matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]))