class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        check = False
        if num < 0:
            num = str(num)[1:] 
            check = True
        else:
            num = str(num)
        
        dum = [int(i) for i in num]
        dum = sorted(dum) 
        
        if check:
            dum = dum[::-1]
            val = '-' + ''.join(map(str, dum))
            return int(val)
        
        if dum[0] == 0:
            for i in range(len(dum)):
                if dum[i] != 0:
                    dum[0], dum[i] = dum[i], dum[0] 
                    break
        
       
        val = ''.join(map(str, dum))
        return int(val)

s = Solution()
print(s.smallestNumber(2932))  # Output: 2239
print(s.smallestNumber(-2932))  # Output: -9223
