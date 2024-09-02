class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        dum=[first]
        
        for i in range(0,len(encoded)):
            dum.append(encoded[i]^dum[i])
        print(dum)
        

s=Solution()
s.decode(encoded = [1,2,3], first = 1)