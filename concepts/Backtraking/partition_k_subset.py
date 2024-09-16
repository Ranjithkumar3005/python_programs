class Solution:
    def canPartitionKSubsets(self, nums, k):
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        target = total_sum // k  # Each subset needs to sum to this value
        nums.sort(reverse=True)  # Sorting in descending order helps speed up backtracking
        sides = [0] * k  # Initialize array to hold sums of each partition
        
        def backtrack(i):
            if i == len(nums):
                # Check if all subsets match the target sum
                return all(side == target for side in sides)
            
            for j in range(k):
                if sides[j] + nums[i] <= target:
                    sides[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] -= nums[i]  # Backtrack
                    
                # Optimization: If a subset remains empty after trying to place the current number, no need to continue
                if sides[j] == 0:
                    break
            
            return False
        
        return backtrack(0)
        


s=Solution()
print(s.canPartitionKSubsets(nums = [4,3,2,3,5,2,1], k = 4))