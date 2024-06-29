
class Solution:
    def searchInsert(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] < target:
                low = mid + 1  # Adjust low pointer
            else:
                high = mid - 1  # Adjust high pointer

        return low  # Return the index for insertion position
        
        
s=Solution()
s.searchInsert(nums = [1,3,5,6], target = 5)