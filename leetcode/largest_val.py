class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        dum=[0]*(len(gain)+1)
        for i in range(0,len(gain)):
            dum[i+1]=dum[i]+gain[i]
        return max(dum)
        

s=Solution()
s.largestAltitude(gain = [-5,1,5,0,-7])