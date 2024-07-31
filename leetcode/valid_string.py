class Solution:
    def validStrings(self, n):
        l=[]
        for i in range(1 << n):
            binary_str = format(i, '0' + str(n) + 'b')
            if("00" not in binary_str):
                l.append(binary_str)
        return l
    
    

s=Solution()
print(s.validStrings(n=3))