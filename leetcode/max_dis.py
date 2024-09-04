class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i,j=0,0
        res = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                res=  max(res,j-i)
                j += 1
        return res

# Example usage:
s = Solution()
print(s.maxDistance(nums1=[55, 30, 5, 4, 2], nums2=[100, 20, 10, 10, 5]))  # Output: 2
