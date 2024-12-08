class Solution:
    def largestNumber(self, num):
        num = list(num)
        n = len(num)

        def sort_segment(start, end):
            segment = sorted(num[start : end + 1], reverse=True)
            num[start : end + 1] = segment

        i = 0
        while i < n:
            j = i
            while j + 1 < n and (int(num[j]) % 2 == int(num[j + 1]) % 2):
                j += 1
            sort_segment(i, j)
            i = j + 1
        return "".join(num)
#


