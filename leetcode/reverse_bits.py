class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = format(n, 'b')
        n = n.zfill(32)
        return int(n[::-1], 2)
        
        

s=Solution()
print(s.reverseBits(n = 0b00000010100101000001111010011100))