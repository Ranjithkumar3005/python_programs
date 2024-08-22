class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        dum=[]
        for i in arr:
            dum.append(i)
            if dum in pieces:
                pieces.remove(dum)
                dum=[]
        if pieces==[]:
            return True
        return False
        

s=Solution()
print(s.canFormArray( arr = [91,4,64,78], pieces = [[78],[4,64],[91]]))