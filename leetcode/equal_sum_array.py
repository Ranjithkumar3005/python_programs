class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if sum1 > sum2:
            nums1, nums2 = nums2, nums1
            sum1, sum2 = sum2, sum1
        diff = sum2 - sum1
        dum = []
        for i in nums1:
            dum.append(6 - i)
        for i in nums2:
            dum.append(i - 1)
        dum = sorted(dum, reverse=True)
        op = 0
        i = 0
        while diff > 0:
            if i == len(dum):
                return -1
            diff -= dum[i]
            i += 1
            op += 1
        return op
