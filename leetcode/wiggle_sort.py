class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()  # Sort the array
        n = len(nums)

        result = [0] * n

        mid = (n + 1) // 2  # Middle index for the sorted array
        left = mid - 1  # Pointer for the left half (smaller elements)
        right = n - 1  # Pointer for the right half (larger elements)

        for i in range(n):
            if i % 2 == 0:  # For even indices
                result[i] = nums[left]
                left -= 1
            else:  # For odd indices
                result[i] = nums[right]
                right -= 1

        for i in range(n):
            nums[i] = result[i]


# Example usage
s = Solution()
s.wiggleSort(nums=[1, 3, 2, 2, 3, 1])
