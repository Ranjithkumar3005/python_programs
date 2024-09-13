class Solution(object):
    def palindrom(self, num):
        s=str(num)        
        while s!=s[::-1]:
            s=str(int(s)+int(s[::-1]))
        print(s)
        
s=Solution()
s.palindrom(148)