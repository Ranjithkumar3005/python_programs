class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max1=0
        c=0
        for i in s:
            if i=="E":
                c+=1
                max1=max(max1,c)
            else:
                c-=1
        print(max1)

s=Solution()
s.minimumChairs(s = "EEEEEE")