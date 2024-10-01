class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        h = {}
        for i in range(len(arr)):
            rem = arr[i] % k
            if rem in h:
                h[rem] += 1
            else:
                h[rem] = 1

        for r in h:
            if r == 0:
                if h[r] % 2 != 0:
                    return False
            else:
                if h[r] != h[(k - r) % k]:
                    return False

        return True


s = Solution()
s.canArrange(arr=[1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k=5)
