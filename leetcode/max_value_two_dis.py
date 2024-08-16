class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        max_val = 0
        for sign1 in [1, -1]:
            for sign2 in [1, -1]:
                smallest = sign1 * arr1[0] + sign2 * arr2[0] + 0
                for i in range(len(arr1)):
                    current = sign1 * arr1[i] + sign2 * arr2[i] + i
                    max_val = max(max_val, current - smallest)
                    smallest = min(smallest, current)
        
        return max_val

        
        

s=Solution()
s.maxAbsValExpr( arr1 = [1,2,3,4], arr2 = [-1,4,5,6])