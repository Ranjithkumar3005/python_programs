class Solution:
    def check(self, s):
        tot = 0
        str1 = "0"

        for i in s:
            if i.isdigit():
                str1 += i
            else:
                tot += int(str1)
                str1 = "0"
        tot += int(str1)
        print(tot)


s = Solution()
s.check("1xyz23vvv6")
