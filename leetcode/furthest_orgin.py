class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        c=0
        tot=0
        for i in range(0,len(moves)):
            if moves[i]=="_":
                c+=1
            if moves[i]=="L":
                tot-=1
            if moves[i]=="R":
                tot+=1
        return c+abs(tot)
        

s=Solution()
print(s.furthestDistanceFromOrigin( moves = "L_RL__R"))