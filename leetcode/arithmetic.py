class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr=sorted(arr)
        sum=arr[0]-arr[1]
        for i in range(1,len(arr)-1):
            print()
            if sum != arr[i]-arr[i+1]:
                return False
        return True
    
    

s=Solution()
s.canMakeArithmeticProgression(arr = [1,2,4])