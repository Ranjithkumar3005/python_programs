import math
class Solution(object):
    def permute(self, nums):
        """
        :type arr: List[int]
    a    :rtype: List[List[int]]
        """
        def arras(arr):
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
               i -= 1
            if i >= 0:
              j = len(arr) - 1
              while arr[j] <= arr[i]:
                j -= 1
              arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1:] = reversed(arr[i + 1:])
            return arr
        final=[]
        dum=nums
        h={}
        n=math.factorial(len(nums))
        for i in range(0,n):
            dum=arras(dum[::])
            if str(dum) not in h:
              final.append(dum)
              h[str(dum)]=0
        
        print(final)

s=Solution()
s.permute(nums = [1,1,2])