class Solution(object):
    def minimumLevels(self, possible):
        """
        :type possible: List[int]
        :rtype: int
        """
        if possible[0]==0:
            alice=-1
        else:
            alice=1
        
        bob=0
        for i in range(1,len(possible)):
            if possible[i]==0:
                bob-=1
            else:
                bob+=1
        if alice>bob:
            return 1
        
        c=1
        for i in range(1,len(possible)):
            
            if possible[i]==0:
                alice-=1
                bob+=1
            else:
                alice+=1
                bob-=1
            c+=1
            if alice>bob and c!=len(possible):
                return c 
        
        
        return -1
        
        

s=Solution()
print(s.minimumLevels([1,1]))