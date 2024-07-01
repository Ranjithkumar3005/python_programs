class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if(len(arr)<3):
            return False
        for i in range(0,len(arr)-2):
            if(arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0):
                return True
        
        return False
        
        

s=Solution()
print(s.threeConsecutiveOdds(arr = [6,3,2,2,3,4,6]))