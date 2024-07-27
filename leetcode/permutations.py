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
        n=math.factorial(len(nums))
        for i in range(0,n):
            dum=arras(dum[::])
            final.append(dum)
        
        print(final)

s=Solution()
s.permute(nums = [0,1])