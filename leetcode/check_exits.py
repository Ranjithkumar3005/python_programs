class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        for i in range(0,len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[i]==2*arr[j]:
                    return True
        return False

s=Solution()
print(s.checkIfExist(arr = [10,2,5,3]))