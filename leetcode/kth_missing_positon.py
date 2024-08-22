class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        arr_set = set(arr)  # Convert the list to a set for O(1) lookups
        count = 0
        current = 1
        
        while count < k:
            if current not in arr_set:
                count += 1
            if count == k:
                return current
            current += 1
        
        return -1
            
        

s=Solution()
print(s.findKthPositive(arr = [2,3,4,7,11], k = 5))