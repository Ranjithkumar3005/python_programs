class Solution(object):
    def checkpalidorm(self, nums):
        str1=""
        for i in nums:
            if i.isalnum():
                str1+=i.lower()
        return str1==str1[::-1]
        

s=Solution()
print(s.checkpalidorm("A man, a plan, a canal: Panama"))