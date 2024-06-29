class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        arr = [i for i in arr if arr.count(i) == 1]
        return "" if k > len(arr) else arr[k - 1]
            
s=Solution()
print(s.kthDistinct(arr =["aaa","aa","a"],k =1))