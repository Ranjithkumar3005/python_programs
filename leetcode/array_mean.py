class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        len1 = len(arr) // 20  # This is equivalent to 5% of the array length
        trimmed_sum = sum(arr[len1:-len1])
        trimmed_length = len(arr) - 2 * len1
        return trimmed_sum / trimmed_length
        

s=Solution()
print(s.trimMean( arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]))