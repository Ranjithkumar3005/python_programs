class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        
        c=0
        for i in commands:
            if i=="DOWN":
                c+=n
            elif i=="RIGHT":
                c+=1
            elif i=="UP":
                c-=n
            else:
                c-=1
        print(c)
        
        

s=Solution()
s.finalPositionOfSnake( n = 3, commands = ["DOWN","RIGHT","UP"])