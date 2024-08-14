from itertools import permutations
class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        arr = list(permutations(sorted(arr, reverse=True)))
        print(arr)
        for h1, h2, m1, m2 in arr:
            if h1 * 10 + h2 < 24 and m1 * 10 + m2 < 60:
                return f'{h1}{h2}:{m1}{m2}'
        return ''
        
        

s=Solution()
print(s.largestTimeFromDigits(arr = [1,2,3,4]))