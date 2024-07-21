class Solution(object):
    def losingPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        c=0
        while True:
            if x>0 and y>=4:
                x-=1
                y-=4
                c+=1
                
            else:
                break
        if c%2==0:
            return "Bob"
        else:
            return "Alice"
        

s=Solution()
print(s.losingPlayer( x = 2, y = 7))