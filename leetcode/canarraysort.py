class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        dums = sorted(nums)
        # if nums==dums:
        #     return True
        h = {}
        h1 = {}
        for i in range(0, len(nums)):
            val = bin(nums[i]).count("1")
            if val in h:
                h[val].append(i)
                d = dums.index(nums[i])
                h1[val].append(d)
                dums[d] = -1

            else:
                h[val] = [i]
                d = dums.index(nums[i])
                h1[val] = [d]
                dums[d] = -1
        for i in h:
            ch2 = sorted(h1[i])
            if h[i] != ch2:
                return False
            for j in range(0, len(h[i]) - 1):
                if h[i][j] != h1[i][j]:
                    if (h[i][j + 1] - h[i][j]) > 1:
                        return False
        return True
