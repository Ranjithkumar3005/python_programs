class Solution:
    def reverse(self):
        for i in range(1,101):
            tot=i*i
            tot1=int(str(i)[::-1])
            if tot==tot1*tot1:
                print(i)

s=Solution()
s.reverse()