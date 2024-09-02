class Solution:
    def waysToMakeFair(self, nums):
        n = len(nums)
        evenSum = [0] * (n + 1)
        oddSum = [0] * (n + 1)
        
        for i in range(n):
            evenSum[i + 1] = evenSum[i]
            oddSum[i + 1] = oddSum[i]
            if i % 2 == 0:
                evenSum[i + 1] += nums[i]
            else:
                oddSum[i + 1] += nums[i]
        print(evenSum)
        count = 0
        
        for i in range(n):
            evenLeft = evenSum[i] + (oddSum[n] - oddSum[i + 1])
            oddLeft = oddSum[i] + (evenSum[n] - evenSum[i + 1])
            
            if evenLeft == oddLeft:
                count += 1
        
        return count


s = Solution()
result = s.waysToMakeFair([2,1,6,4])
print(result) 