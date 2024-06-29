class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        i=j=0
        dummy={(0,0)}
        for c in path:
            match c:
                case 'N':
                    i-=1
                case 'S':
                    i+=1
                case 'E':
                    j+=1
                case 'W':
                    j-=1
            if (i,j) in dummy:
                return True
            dummy.add((i,j))
        return False
        
        
s=Solution()
print(s.isPathCrossing(path = "NESWW"))