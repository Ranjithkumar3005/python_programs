class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<3:
            return False
        check=False
        for i in range(0,len(arr)-1):
            if not check:
                if arr[i]>=arr[i+1]:
                    check=True
            if check:
                if arr[i]<=arr[i+1]:
                    return False
                
        return True
        

s=Solution()
print(s.validMountainArray( arr = [0,3,2,1]))