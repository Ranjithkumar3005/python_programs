from collections import Counter

class Solution(object):
    def numTriplets(self, nums1, nums2):
        def count_pairs(nums1, nums2):
            count = 0
            square_count = Counter()
            
            for num in nums1:
                square_count[num * num] += 1
            
            for i in range(len(nums2)):
                for j in range(i + 1, len(nums2)):
                    product = nums2[i] * nums2[j]
                    count += square_count[product]
            
            return count
        return count_pairs(nums1, nums2) + count_pairs(nums2, nums1)

# Test the solution
s = Solution()
print(s.numTriplets(nums1 = [7, 4], nums2 = [5, 2, 8, 9]))
