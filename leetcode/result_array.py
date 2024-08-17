class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        results = []
        
        for i in range(len(nums) - k + 1):
            subarray = nums[i:i + k]
            
            if all(subarray[j] + 1 == subarray[j + 1] for j in range(len(subarray) - 1)):
                results.append(max(subarray))
            else:
                results.append(-1)
        
        return results

# Example usage:
s = Solution()
print(s.resultsArray(nums=[1, 2, 3, 4, 3, 2, 5], k=3))  # Output: [3, 4, -1, -1, -1]
