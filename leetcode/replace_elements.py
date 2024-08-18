class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        maxRight = -1 
        for i in range(n - 1, -1, -1):
            current = arr[i]
            arr[i] = maxRight
            maxRight = max(maxRight, current)
        
        return arr

s=Solution()
s.replaceElements(arr = [17,18,5,4,6,1])