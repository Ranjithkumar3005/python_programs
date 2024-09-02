class Solution:
    def minSubarray(self, nums, p):
        totalSum = sum(nums)
        remainder = totalSum % p
        
        if remainder == 0:
            return 0
        
        prefixSum = 0
        minLength = len(nums)
        prefixMap = {0: -1} 
        for i, num in enumerate(nums):
            prefixSum = (prefixSum + num) % p
            target = (prefixSum - remainder) % p
            
            if target in prefixMap:
                minLength = min(minLength, i - prefixMap[target])
            
            prefixMap[prefixSum] = i
        print(prefixMap)
        return minLength if minLength < len(nums) else -1

s = Solution()
result = s.minSubarray([3, 1, 4, 2], 6)
print(result) 